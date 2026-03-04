from fastmcp import FastMCP
from mock_data.performance import PERFORMANCE
from mock_data.holdings import FUNDS

VALID_PERIODS = ["1d", "1w", "mtd", "qtd", "ytd", "1y", "3y", "itd"]

mcp = FastMCP()


@mcp.tool
def get_fund_performance(fund: str, period: str = "ytd") -> dict:
    """
    Return fund return vs benchmark for a given period.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    Available periods: 1d, 1w, mtd (month-to-date), qtd (quarter-to-date),
                       ytd (year-to-date), 1y, 3y, itd (inception-to-date)
    """
    fund = fund.upper()
    period = period.lower()

    if fund not in FUNDS:
        return {"error": f"Unknown fund '{fund}'. Available funds: {', '.join(FUNDS)}"}
    if period not in VALID_PERIODS:
        return {"error": f"Unknown period '{period}'. Valid periods: {', '.join(VALID_PERIODS)}"}

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
        return {"error": f"Unknown fund '{fund}'. Available funds: {', '.join(FUNDS)}"}

    perf = PERFORMANCE[fund]
    if period not in perf.get("attribution", {}):
        return {"error": f"Attribution not available for period '{period}' on fund '{fund}'."}

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
