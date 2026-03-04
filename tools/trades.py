from mock_data.trades import TRADE_BLOTTER, DATA_AS_OF
from mock_data.holdings import FUNDS


def get_trade_blotter(fund: str | None = None, date: str | None = None) -> dict:
    """
    Return the trade blotter showing all executed trades. Can be filtered by
    fund and/or date (YYYY-MM-DD format). Returns all trades if no filters applied.

    Available funds: ALPHA-1, ALPHA-2, MACRO-GLOBAL
    Most recent trading date: 2026-03-03
    """
    trades = TRADE_BLOTTER

    if fund:
        fund = fund.upper()
        if fund not in FUNDS:
            return {"error": f"Unknown fund '{fund}'. Available funds: {', '.join(FUNDS)}"}
        trades = [t for t in trades if t["fund"] == fund]

    if date:
        trades = [t for t in trades if t["date"] == date]

    if not trades:
        return {
            "fund": fund,
            "date": date,
            "as_of": str(DATA_AS_OF),
            "message": "No trades found for the given filters.",
            "trades": [],
        }

    total_buy_notional = sum(t["notional"] for t in trades if t["direction"] == "BUY")
    total_sell_notional = sum(t["notional"] for t in trades if t["direction"] == "SELL")
    net_notional = total_buy_notional - total_sell_notional

    return {
        "fund_filter": fund or "ALL",
        "date_filter": date or "ALL",
        "as_of": str(DATA_AS_OF),
        "trade_count": len(trades),
        "total_buy_notional": round(total_buy_notional, 2),
        "total_sell_notional": round(total_sell_notional, 2),
        "net_notional": round(net_notional, 2),
        "trades": sorted(trades, key=lambda x: (x["date"], x["fund"]), reverse=True),
    }
