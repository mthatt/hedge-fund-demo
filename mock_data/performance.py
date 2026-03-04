PERFORMANCE = {
    "ALPHA-1": {
        "nav": 1599800000,
        "nav_per_share": 142.86,
        "inception_date": "2019-01-15",
        "benchmark": "S&P 500",
        "returns": {
            "1d":   {"fund": 0.42,  "benchmark": 0.31},
            "1w":   {"fund": 1.18,  "benchmark": 0.87},
            "mtd":  {"fund": 2.74,  "benchmark": 1.95},
            "qtd":  {"fund": 4.21,  "benchmark": 3.10},
            "ytd":  {"fund": 6.83,  "benchmark": 4.72},
            "1y":   {"fund": 18.42, "benchmark": 14.30},
            "3y":   {"fund": 42.10, "benchmark": 35.20},
            "itd":  {"fund": 87.30, "benchmark": 65.40},
        },
        "attribution": {
            "mtd": [
                {"name": "NVDA",  "contribution_pct": 1.12, "return_pct": 14.20},
                {"name": "BRK.B", "contribution_pct": 0.58, "return_pct": 6.40},
                {"name": "META",  "contribution_pct": 0.43, "return_pct": 11.30},
                {"name": "GLD",   "contribution_pct": 0.38, "return_pct": 4.60},
                {"name": "SPY",   "contribution_pct": 0.32, "return_pct": 2.90},
                {"name": "LLY",   "contribution_pct": -0.12, "return_pct": -4.50},
                {"name": "TLT",   "contribution_pct": -0.18, "return_pct": -3.90},
                {"name": "Other", "contribution_pct": 0.21, "return_pct": None},
            ]
        },
    },
    "ALPHA-2": {
        "nav": 919080000,
        "nav_per_share": 98.12,
        "inception_date": "2021-06-01",
        "benchmark": "NASDAQ 100",
        "returns": {
            "1d":   {"fund": 0.61,  "benchmark": 0.55},
            "1w":   {"fund": 2.30,  "benchmark": 1.90},
            "mtd":  {"fund": 5.10,  "benchmark": 3.80},
            "qtd":  {"fund": 7.40,  "benchmark": 5.20},
            "ytd":  {"fund": 10.20, "benchmark": 7.10},
            "1y":   {"fund": 28.40, "benchmark": 22.10},
            "3y":   {"fund": 31.20, "benchmark": 28.40},
            "itd":  {"fund": 42.80, "benchmark": 38.10},
        },
        "attribution": {
            "mtd": [
                {"name": "AAPL",  "contribution_pct": 1.85, "return_pct": 14.90},
                {"name": "NFLX",  "contribution_pct": 1.20, "return_pct": 19.90},
                {"name": "AMD",   "contribution_pct": 0.95, "return_pct": 16.30},
                {"name": "TSLA",  "contribution_pct": 0.62, "return_pct": 11.50},
                {"name": "V",     "contribution_pct": 0.30, "return_pct": 5.20},
                {"name": "CRM",   "contribution_pct": -0.08, "return_pct": -1.50},
                {"name": "Other", "contribution_pct": 0.26, "return_pct": None},
            ]
        },
    },
    "MACRO-GLOBAL": {
        "nav": 600000000,
        "nav_per_share": 115.30,
        "inception_date": "2020-03-01",
        "benchmark": "HFRX Global Hedge Fund Index",
        "returns": {
            "1d":   {"fund": 0.28,  "benchmark": 0.12},
            "1w":   {"fund": 0.94,  "benchmark": 0.40},
            "mtd":  {"fund": 3.20,  "benchmark": 1.10},
            "qtd":  {"fund": 5.80,  "benchmark": 2.30},
            "ytd":  {"fund": 8.10,  "benchmark": 3.40},
            "1y":   {"fund": 12.40, "benchmark": 5.80},
            "3y":   {"fund": 28.60, "benchmark": 14.20},
            "itd":  {"fund": 52.10, "benchmark": 22.80},
        },
        "attribution": {
            "mtd": [
                {"name": "GLD",   "contribution_pct": 1.92, "return_pct": 4.40},
                {"name": "EFA",   "contribution_pct": 0.72, "return_pct": 6.90},
                {"name": "EEM",   "contribution_pct": 0.48, "return_pct": 6.80},
                {"name": "USO",   "contribution_pct": 0.22, "return_pct": 3.60},
                {"name": "UUP",   "contribution_pct": -0.08, "return_pct": -1.70},
                {"name": "TLT",   "contribution_pct": -0.14, "return_pct": -1.50},
                {"name": "Other", "contribution_pct": 0.08, "return_pct": None},
            ]
        },
    },
}
