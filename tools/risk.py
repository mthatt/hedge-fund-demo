from fastmcp import FastMCP
from mock_data.risk import RISK_METRICS, LIQUIDITY
from mock_data.holdings import FUNDS

mcp = FastMCP()


@mcp.tool
def get_risk_metrics(fund: str) -> dict:
    """
    Return key risk metrics for a fund: Value at Risk (VaR), volatility,
    Sharpe ratio, Sortino ratio, max drawdown, and beta to S&P 500.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    VaR is calculated using historical simulation over a 1-year lookback.
    """
    fund = fund.upper()
    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available funds: {', '.join(FUNDS)}"}

    r = RISK_METRICS[fund]
    return {
        "fund": fund,
        "var": {
            "description": "Estimated maximum loss at given confidence level over holding period",
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
    Return the fund's exposure to common systematic risk factors:
    market beta, size, value, momentum, quality, low volatility, and growth.

    Exposures are z-scores relative to the benchmark universe.
    Positive = tilted toward factor, Negative = tilted away.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    """
    fund = fund.upper()
    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available funds: {', '.join(FUNDS)}"}

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
        "methodology": "Z-score relative to benchmark universe, 90-day estimation window",
    }


@mcp.tool
def get_liquidity_analysis(fund: str) -> dict:
    """
    Return a liquidity analysis showing how many days it would take to unwind
    each position, assuming we trade 20% of average daily volume (ADV) per day.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    """
    fund = fund.upper()
    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available funds: {', '.join(FUNDS)}"}

    liq = LIQUIDITY[fund]
    positions = sorted(liq["positions"], key=lambda x: -x["days_to_liquidate"])

    illiquid = [p for p in positions if p["days_to_liquidate"] > 1]

    return {
        "fund": fund,
        "summary": liq["portfolio_summary"],
        "positions": positions,
        "illiquid_positions": illiquid,
        "assumption": "Positions liquidated at 20% of average daily volume (ADV) per day",
    }
