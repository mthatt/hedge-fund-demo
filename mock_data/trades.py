from datetime import date

TRADE_BLOTTER = [
    # Date, Fund, Ticker, Direction, Shares, Price, Notional, Trader, Strategy, Status
    {"date": "2026-03-03", "fund": "ALPHA-1",      "ticker": "NVDA",  "direction": "BUY",  "shares": 10000,  "price": 875.40,  "notional": 8754000,   "trader": "S. Chen",    "strategy": "Long Growth",    "status": "FILLED"},
    {"date": "2026-03-03", "fund": "ALPHA-1",      "ticker": "TLT",   "direction": "SELL", "shares": 50000,  "price": 92.30,   "notional": 4615000,   "trader": "S. Chen",    "strategy": "Risk Reduction", "status": "FILLED"},
    {"date": "2026-03-03", "fund": "ALPHA-2",      "ticker": "AAPL",  "direction": "BUY",  "shares": 25000,  "price": 228.70,  "notional": 5717500,   "trader": "M. Patel",   "strategy": "Long Growth",    "status": "FILLED"},
    {"date": "2026-03-03", "fund": "ALPHA-2",      "ticker": "TSLA",  "direction": "SELL", "shares": 15000,  "price": 248.50,  "notional": 3727500,   "trader": "M. Patel",   "strategy": "Trim Winner",    "status": "FILLED"},
    {"date": "2026-03-03", "fund": "MACRO-GLOBAL", "ticker": "GLD",   "direction": "BUY",  "shares": 50000,  "price": 218.50,  "notional": 10925000,  "trader": "R. Torres",  "strategy": "Gold Long",      "status": "FILLED"},
    {"date": "2026-03-03", "fund": "MACRO-GLOBAL", "ticker": "UUP",   "direction": "SELL", "shares": 100000, "price": 28.60,   "notional": 2860000,   "trader": "R. Torres",  "strategy": "USD Short",      "status": "FILLED"},

    {"date": "2026-03-02", "fund": "ALPHA-1",      "ticker": "META",  "direction": "BUY",  "shares": 8000,   "price": 502.10,  "notional": 4016800,   "trader": "S. Chen",    "strategy": "Long Growth",    "status": "FILLED"},
    {"date": "2026-03-02", "fund": "ALPHA-1",      "ticker": "LLY",   "direction": "SELL", "shares": 5000,   "price": 735.20,  "notional": 3676000,   "trader": "S. Chen",    "strategy": "Trim Winner",    "status": "FILLED"},
    {"date": "2026-03-02", "fund": "ALPHA-2",      "ticker": "NFLX",  "direction": "BUY",  "shares": 6000,   "price": 685.40,  "notional": 4112400,   "trader": "M. Patel",   "strategy": "Long Growth",    "status": "FILLED"},
    {"date": "2026-03-02", "fund": "ALPHA-2",      "ticker": "CRM",   "direction": "BUY",  "shares": 10000,  "price": 318.20,  "notional": 3182000,   "trader": "M. Patel",   "strategy": "Long Growth",    "status": "FILLED"},
    {"date": "2026-03-02", "fund": "MACRO-GLOBAL", "ticker": "EEM",   "direction": "BUY",  "shares": 80000,  "price": 41.90,   "notional": 3352000,   "trader": "R. Torres",  "strategy": "EM Long",        "status": "FILLED"},
    {"date": "2026-03-02", "fund": "MACRO-GLOBAL", "ticker": "TLT",   "direction": "SELL", "shares": 40000,  "price": 92.80,   "notional": 3712000,   "trader": "R. Torres",  "strategy": "Duration Short", "status": "FILLED"},

    {"date": "2026-02-28", "fund": "ALPHA-1",      "ticker": "XOM",   "direction": "BUY",  "shares": 30000,  "price": 106.50,  "notional": 3195000,   "trader": "S. Chen",    "strategy": "Energy Long",    "status": "FILLED"},
    {"date": "2026-02-28", "fund": "ALPHA-1",      "ticker": "GOOGL", "direction": "SELL", "shares": 20000,  "price": 170.10,  "notional": 3402000,   "trader": "S. Chen",    "strategy": "Trim Winner",    "status": "FILLED"},
    {"date": "2026-02-28", "fund": "ALPHA-2",      "ticker": "AMD",   "direction": "BUY",  "shares": 20000,  "price": 174.30,  "notional": 3486000,   "trader": "M. Patel",   "strategy": "Semi Long",      "status": "FILLED"},
    {"date": "2026-02-28", "fund": "MACRO-GLOBAL", "ticker": "USO",   "direction": "BUY",  "shares": 50000,  "price": 71.20,   "notional": 3560000,   "trader": "R. Torres",  "strategy": "Oil Long",       "status": "FILLED"},
    {"date": "2026-02-28", "fund": "MACRO-GLOBAL", "ticker": "EFA",   "direction": "BUY",  "shares": 60000,  "price": 77.80,   "notional": 4668000,   "trader": "R. Torres",  "strategy": "DM Long",        "status": "FILLED"},
]

DATA_AS_OF = date(2026, 3, 3)
