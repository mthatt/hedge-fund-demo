from fastmcp import FastMCP
from mock_data.holdings import HOLDINGS, FUNDS, DATA_AS_OF

mcp = FastMCP()


@mcp.tool
def get_portfolio_holdings(fund: str) -> dict:
    """
    Return the current holdings for a given fund, including ticker, sector,
    market value, portfolio weight, and unrealized P&L per position.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    Data is as of the previous market close.
    """
    fund = fund.upper()
    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available funds: {', '.join(FUNDS)}"}

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
    Return the portfolio's exposure breakdown by sector as a percentage of NAV.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    """
    fund = fund.upper()
    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available funds: {', '.join(FUNDS)}"}

    positions = HOLDINGS[fund]
    total_nav = sum(p["market_value"] for p in positions)

    sector_map: dict[str, float] = {}
    for p in positions:
        sector = p["sector"]
        sector_map[sector] = sector_map.get(sector, 0) + p["market_value"]

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
