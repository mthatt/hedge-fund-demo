from fastmcp import FastMCP
from tools.portfolio import get_portfolio_holdings, get_sector_exposure
from tools.performance import get_fund_performance, get_performance_attribution
from tools.risk import get_risk_metrics, get_factor_exposures, get_liquidity_analysis
from tools.trades import get_trade_blotter

mcp = FastMCP(
    name="Hedge Fund Data Platform",
    instructions="""
    You are a data assistant for a hedge fund. You have access to portfolio,
    performance, risk, and trading data for three funds: ALPHA-1, ALPHA-2, and MACRO-GLOBAL.

    Use the available tools to answer questions from portfolio managers, risk managers,
    traders, and compliance officers. Always cite the 'as_of' date when presenting data.
    Present numbers clearly: format large dollar values with commas and $ prefix,
    percentages with a % suffix, and round to 2 decimal places.
    """,
)

mcp.tool(get_portfolio_holdings)
mcp.tool(get_sector_exposure)
mcp.tool(get_fund_performance)
mcp.tool(get_performance_attribution)
mcp.tool(get_risk_metrics)
mcp.tool(get_factor_exposures)
mcp.tool(get_liquidity_analysis)
mcp.tool(get_trade_blotter)


@mcp.tool
def get_data_freshness() -> dict:
    """
    Return the last refresh timestamp for each data source in the platform.
    Use this to confirm whether the data you're looking at is up to date.
    """
    return {
        "as_of_note": "All timestamps are US/Eastern. Data refreshes at 7:00 AM ET on trading days.",
        "sources": {
            "holdings": {
                "last_updated": "2026-03-03 07:02:14 ET",
                "source": "Prime Broker Feed (Goldman Sachs)",
                "latency": "T+0, end-of-day positions",
                "status": "OK",
            },
            "performance": {
                "last_updated": "2026-03-03 07:04:38 ET",
                "source": "Internal NAV Calculation Engine",
                "latency": "T+0, end-of-day",
                "status": "OK",
            },
            "risk_metrics": {
                "last_updated": "2026-03-03 07:18:52 ET",
                "source": "Risk System (Axioma)",
                "latency": "T+0, recalculated nightly",
                "status": "OK",
            },
            "factor_exposures": {
                "last_updated": "2026-03-03 07:18:52 ET",
                "source": "Risk System (Axioma)",
                "latency": "T+0, recalculated nightly",
                "status": "OK",
            },
            "trade_blotter": {
                "last_updated": "2026-03-03 16:35:00 ET",
                "source": "OMS (Charles River)",
                "latency": "Real-time during market hours",
                "status": "OK",
            },
            "liquidity": {
                "last_updated": "2026-03-03 07:20:11 ET",
                "source": "Market Data (Bloomberg) + Risk System",
                "latency": "T+0, recalculated nightly",
                "status": "OK",
            },
        },
    }


if __name__ == "__main__":
    mcp.run()
