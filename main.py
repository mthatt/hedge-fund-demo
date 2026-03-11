from __future__ import annotations
from fastmcp import FastMCP
from mock_data.holdings import HOLDINGS, FUNDS, DATA_AS_OF
from mock_data.performance import PERFORMANCE
from mock_data.risk import RISK_METRICS, LIQUIDITY
from mock_data.trades import TRADE_BLOTTER, DATA_AS_OF as TRADES_AS_OF

# ============================================================================
# RISK LIMITS — change these values, redeploy, and watch the agent respond
# differently to "Is MACRO-GLOBAL in compliance?" or "Check risk limits."
#
# Try it: MACRO-GLOBAL holds 43.7% in GLD. With max_position_pct = 15,
# that's a violation. Change it to 50 and redeploy — now it passes.
# ============================================================================
RISK_LIMITS = {
    "max_position_pct": 15,       # max single-position weight (%)
    "max_sector_pct": 40,         # max single-sector weight (%)
    "max_var_95_pct": 2.0,        # max daily VaR at 95% as % of NAV
    "min_liquidity_1d_pct": 50,   # min % of portfolio liquidatable in 1 day
}
# ============================================================================


mcp = FastMCP(
    name="Hedge Fund Data Platform",
    instructions="""
    You are a data assistant for a multi-strategy hedge fund managing three
    funds: ALPHA-1 ($1.6B NAV, long/short equity), ALPHA-2 ($919M NAV,
    tech-focused growth), and MACRO-GLOBAL ($600M NAV, global macro).

    Users are portfolio managers, risk managers, traders, and compliance
    officers. Always cite the as_of date when presenting data.

    Format large dollar values as $X.XXM or $X.XXB with commas.
    Format percentages with one decimal place and a % suffix.
    Round to 2 decimal places unless otherwise noted.
    """,
)

VALID_PERIODS = ["1d", "1w", "mtd", "qtd", "ytd", "1y", "3y", "itd"]


# ---------------------------------------------------------------------------
# Portfolio
# ---------------------------------------------------------------------------


@mcp.tool
def get_portfolio_holdings(fund: str) -> dict:
    """
    Return current holdings for a fund: ticker, sector, market value,
    portfolio weight, and unrealized P&L per position.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    """
    fund = fund.upper()
    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available: {', '.join(FUNDS)}"}

    positions = HOLDINGS[fund]
    enriched = []
    for p in positions:
        unrealized_pnl = (p["price"] - p["cost_basis"]) * p["shares"] if p["ticker"] != "CASH" else 0
        unrealized_pnl_pct = ((p["price"] / p["cost_basis"]) - 1) * 100 if p["ticker"] != "CASH" else 0
        enriched.append({
            **p,
            "unrealized_pnl": round(unrealized_pnl, 2),
            "unrealized_pnl_pct": round(unrealized_pnl_pct, 2),
        })

    total_nav = sum(p["market_value"] for p in positions)

    return {
        "fund": fund,
        "as_of": str(DATA_AS_OF),
        "total_nav": total_nav,
        "position_count": len([p for p in positions if p["ticker"] != "CASH"]),
        "positions": enriched,
    }


@mcp.tool
def get_sector_exposure(fund: str) -> dict:
    """
    Return portfolio exposure breakdown by sector as a percentage of NAV.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    """
    fund = fund.upper()
    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available: {', '.join(FUNDS)}"}

    positions = HOLDINGS[fund]
    total_nav = sum(p["market_value"] for p in positions)

    sector_map: dict[str, float] = {}
    for p in positions:
        sector_map[p["sector"]] = sector_map.get(p["sector"], 0) + p["market_value"]

    sectors = [
        {
            "sector": sector,
            "market_value": round(mv, 2),
            "weight_pct": round((mv / total_nav) * 100, 2),
        }
        for sector, mv in sorted(sector_map.items(), key=lambda x: -x[1])
    ]

    return {
        "fund": fund,
        "as_of": str(DATA_AS_OF),
        "total_nav": total_nav,
        "sectors": sectors,
    }


# ---------------------------------------------------------------------------
# Performance
# ---------------------------------------------------------------------------


@mcp.tool
def get_fund_performance(fund: str, period: str = "ytd") -> dict:
    """
    Return fund return vs benchmark for a given period.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    Available periods: 1d, 1w, mtd, qtd, ytd, 1y, 3y, itd
    """
    fund = fund.upper()
    period = period.lower()

    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available: {', '.join(FUNDS)}"}
    if period not in VALID_PERIODS:
        return {"error": f"Unknown period '{period}'. Valid: {', '.join(VALID_PERIODS)}"}

    perf = PERFORMANCE[fund]
    ret = perf["returns"][period]
    active_return = round(ret["fund"] - ret["benchmark"], 2)

    return {
        "fund": fund,
        "period": period,
        "nav": perf["nav"],
        "nav_per_share": perf["nav_per_share"],
        "benchmark": perf["benchmark"],
        "fund_return_pct": ret["fund"],
        "benchmark_return_pct": ret["benchmark"],
        "active_return_pct": active_return,
        "outperforming": active_return > 0,
        "all_periods": perf["returns"],
    }


@mcp.tool
def get_performance_attribution(fund: str, period: str = "mtd") -> dict:
    """
    Return performance attribution by position — which holdings drove returns
    and by how much (contribution to fund return in percentage points).

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    Available periods: mtd
    """
    fund = fund.upper()
    period = period.lower()

    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available: {', '.join(FUNDS)}"}

    perf = PERFORMANCE[fund]
    if period not in perf.get("attribution", {}):
        return {"error": f"Attribution not available for period '{period}'."}

    attribution = perf["attribution"][period]
    top_contributors = sorted(
        [a for a in attribution if a["contribution_pct"] > 0],
        key=lambda x: -x["contribution_pct"],
    )
    top_detractors = sorted(
        [a for a in attribution if a["contribution_pct"] < 0],
        key=lambda x: x["contribution_pct"],
    )

    return {
        "fund": fund,
        "period": period,
        "total_fund_return_pct": perf["returns"][period]["fund"],
        "benchmark_return_pct": perf["returns"][period]["benchmark"],
        "attribution": attribution,
        "top_contributors": top_contributors,
        "top_detractors": top_detractors,
    }


# ---------------------------------------------------------------------------
# Risk
# ---------------------------------------------------------------------------


@mcp.tool
def get_risk_metrics(fund: str) -> dict:
    """
    Return key risk metrics: Value at Risk (VaR), volatility, Sharpe ratio,
    Sortino ratio, max drawdown, and beta to S&P 500.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    """
    fund = fund.upper()
    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available: {', '.join(FUNDS)}"}

    r = RISK_METRICS[fund]
    return {
        "fund": fund,
        "var": {
            "description": "Estimated maximum loss at given confidence level",
            "confidence_95": r["var"]["confidence_95"],
            "confidence_99": r["var"]["confidence_99"],
        },
        "volatility": {
            "realized_30d_annualized_pct": r["volatility"]["realized_30d"],
            "realized_90d_annualized_pct": r["volatility"]["realized_90d"],
            "implied_annualized_pct": r["volatility"]["implied"],
        },
        "sharpe_ratio": r["sharpe_ratio"],
        "sortino_ratio": r["sortino_ratio"],
        "max_drawdown_pct": r["max_drawdown_pct"],
        "beta_to_spy": r["beta_to_spy"],
        "sector_var_contribution": r["sector_var_contribution"],
    }


@mcp.tool
def get_factor_exposures(fund: str) -> dict:
    """
    Return factor exposures (z-scores): market beta, size, value, momentum,
    quality, low volatility, and growth. Positive = tilted toward factor.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    """
    fund = fund.upper()
    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available: {', '.join(FUNDS)}"}

    exposures = RISK_METRICS[fund]["factor_exposures"]
    annotated = {
        factor: {
            "exposure": score,
            "tilt": "overweight" if score > 0.1 else "underweight" if score < -0.1 else "neutral",
        }
        for factor, score in exposures.items()
    }

    dominant = sorted(exposures.items(), key=lambda x: abs(x[1]), reverse=True)[:3]

    return {
        "fund": fund,
        "factor_exposures": annotated,
        "dominant_factors": [{"factor": f, "exposure": round(e, 2)} for f, e in dominant],
        "methodology": "Z-score relative to benchmark universe, 90-day window",
    }


@mcp.tool
def get_liquidity_analysis(fund: str) -> dict:
    """
    Return liquidity analysis: how many days to unwind each position,
    assuming 20% of average daily volume per day.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    """
    fund = fund.upper()
    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available: {', '.join(FUNDS)}"}

    liq = LIQUIDITY[fund]
    positions = sorted(liq["positions"], key=lambda x: -x["days_to_liquidate"])

    return {
        "fund": fund,
        "summary": liq["portfolio_summary"],
        "positions": positions,
        "illiquid_positions": [p for p in positions if p["days_to_liquidate"] > 1],
        "assumption": "Positions liquidated at 20% of ADV per day",
    }


# ---------------------------------------------------------------------------
# Trading
# ---------------------------------------------------------------------------


@mcp.tool
def get_trade_blotter(fund: str | None = None, date: str | None = None) -> dict:
    """
    Return executed trades, optionally filtered by fund and/or date (YYYY-MM-DD).

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    Most recent trading date: 2026-03-03
    """
    trades = TRADE_BLOTTER

    if fund:
        fund = fund.upper()
        if fund not in FUNDS:
            return {"error": f"Unknown fund '{fund}'. Available: {', '.join(FUNDS)}"}
        trades = [t for t in trades if t["fund"] == fund]

    if date:
        trades = [t for t in trades if t["date"] == date]

    if not trades:
        return {"fund": fund, "date": date, "as_of": str(TRADES_AS_OF), "message": "No trades found.", "trades": []}

    total_buy = sum(t["notional"] for t in trades if t["direction"] == "BUY")
    total_sell = sum(t["notional"] for t in trades if t["direction"] == "SELL")

    return {
        "fund_filter": fund or "ALL",
        "date_filter": date or "ALL",
        "as_of": str(TRADES_AS_OF),
        "trade_count": len(trades),
        "total_buy_notional": round(total_buy, 2),
        "total_sell_notional": round(total_sell, 2),
        "net_notional": round(total_buy - total_sell, 2),
        "trades": sorted(trades, key=lambda x: (x["date"], x["fund"]), reverse=True),
    }


# ---------------------------------------------------------------------------
# Compliance — the demo tool
# ---------------------------------------------------------------------------


@mcp.tool
def check_risk_limits(fund: str) -> dict:
    """
    Check whether a fund is within its risk limits. Returns a pass/fail
    verdict for each limit and an overall compliance status.

    The limits are defined at the top of main.py and can be changed at any
    time. Redeploy after editing to see the agent's response change.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    """
    fund = fund.upper()
    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available: {', '.join(FUNDS)}"}

    positions = HOLDINGS[fund]
    total_nav = sum(p["market_value"] for p in positions)
    risk = RISK_METRICS[fund]
    liq = LIQUIDITY[fund]

    # Position concentration check
    non_cash = [p for p in positions if p["ticker"] != "CASH"]
    worst_position = max(non_cash, key=lambda p: p["weight_pct"])
    position_ok = worst_position["weight_pct"] <= RISK_LIMITS["max_position_pct"]

    # Sector concentration check
    sector_map: dict[str, float] = {}
    for p in positions:
        if p["ticker"] != "CASH":
            sector_map[p["sector"]] = sector_map.get(p["sector"], 0) + p["weight_pct"]
    worst_sector_name = max(sector_map, key=sector_map.get)
    worst_sector_pct = round(sector_map[worst_sector_name], 1)
    sector_ok = worst_sector_pct <= RISK_LIMITS["max_sector_pct"]

    # VaR check
    var_pct = abs(risk["var"]["confidence_95"]["pct"])
    var_ok = var_pct <= RISK_LIMITS["max_var_95_pct"]

    # Liquidity check
    liq_1d = liq["portfolio_summary"]["pct_liquidatable_1d"]
    liq_ok = liq_1d >= RISK_LIMITS["min_liquidity_1d_pct"]

    all_ok = position_ok and sector_ok and var_ok and liq_ok

    return {
        "fund": fund,
        "overall_status": "PASS" if all_ok else "BREACH",
        "limits_applied": RISK_LIMITS,
        "checks": {
            "position_concentration": {
                "status": "PASS" if position_ok else "BREACH",
                "limit": f"{RISK_LIMITS['max_position_pct']}%",
                "actual": f"{worst_position['weight_pct']}%",
                "worst_offender": worst_position["ticker"],
            },
            "sector_concentration": {
                "status": "PASS" if sector_ok else "BREACH",
                "limit": f"{RISK_LIMITS['max_sector_pct']}%",
                "actual": f"{worst_sector_pct}%",
                "worst_offender": worst_sector_name,
            },
            "daily_var_95": {
                "status": "PASS" if var_ok else "BREACH",
                "limit": f"{RISK_LIMITS['max_var_95_pct']}%",
                "actual": f"{var_pct}%",
            },
            "liquidity_1d": {
                "status": "PASS" if liq_ok else "BREACH",
                "limit": f"{RISK_LIMITS['min_liquidity_1d_pct']}%",
                "actual": f"{liq_1d}%",
            },
        },
    }


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------


@mcp.tool
def get_data_freshness() -> dict:
    """
    Return the last refresh timestamp for each data source.
    Use this to confirm whether data is current.
    """
    return {
        "as_of_note": "All timestamps US/Eastern. Data refreshes at 7:00 AM ET on trading days.",
        "sources": {
            "holdings":         {"last_updated": "2026-03-03 07:02:14 ET", "source": "Prime Broker (Goldman Sachs)",  "status": "OK"},
            "performance":      {"last_updated": "2026-03-03 07:04:38 ET", "source": "NAV Calculation Engine",        "status": "OK"},
            "risk_metrics":     {"last_updated": "2026-03-03 07:18:52 ET", "source": "Risk System (Axioma)",           "status": "OK"},
            "factor_exposures": {"last_updated": "2026-03-03 07:18:52 ET", "source": "Risk System (Axioma)",           "status": "OK"},
            "trade_blotter":    {"last_updated": "2026-03-03 16:35:00 ET", "source": "OMS (Charles River)",            "status": "OK"},
            "liquidity":        {"last_updated": "2026-03-03 07:20:11 ET", "source": "Bloomberg + Risk System",        "status": "OK"},
        },
    }


if __name__ == "__main__":
    mcp.run()
