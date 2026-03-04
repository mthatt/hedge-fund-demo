from datetime import date

FUNDS = ["ALPHA-1", "ALPHA-2", "MACRO-GLOBAL"]

HOLDINGS = {
    "ALPHA-1": [
        {"ticker": "NVDA", "name": "NVIDIA Corporation", "sector": "Information Technology", "shares": 150000, "price": 875.40, "market_value": 131310000, "weight_pct": 8.21, "cost_basis": 620.00},
        {"ticker": "MSFT", "name": "Microsoft Corporation", "sector": "Information Technology", "shares": 200000, "price": 415.20, "market_value": 83040000, "weight_pct": 5.19, "cost_basis": 380.00},
        {"ticker": "GOOGL", "name": "Alphabet Inc.", "sector": "Communication Services", "shares": 180000, "price": 172.30, "market_value": 31014000, "weight_pct": 1.94, "cost_basis": 140.00},
        {"ticker": "JPM", "name": "JPMorgan Chase & Co.", "sector": "Financials", "shares": 250000, "price": 198.50, "market_value": 49625000, "weight_pct": 3.10, "cost_basis": 155.00},
        {"ticker": "UNH", "name": "UnitedHealth Group", "sector": "Health Care", "shares": 80000, "price": 512.30, "market_value": 40984000, "weight_pct": 2.56, "cost_basis": 490.00},
        {"ticker": "LLY", "name": "Eli Lilly and Company", "sector": "Health Care", "shares": 60000, "price": 730.10, "market_value": 43806000, "weight_pct": 2.74, "cost_basis": 580.00},
        {"ticker": "AMZN", "name": "Amazon.com Inc.", "sector": "Consumer Discretionary", "shares": 300000, "price": 192.40, "market_value": 57720000, "weight_pct": 3.61, "cost_basis": 170.00},
        {"ticker": "META", "name": "Meta Platforms Inc.", "sector": "Communication Services", "shares": 120000, "price": 505.60, "market_value": 60672000, "weight_pct": 3.79, "cost_basis": 330.00},
        {"ticker": "BRK.B", "name": "Berkshire Hathaway Inc.", "sector": "Financials", "shares": 400000, "price": 362.10, "market_value": 144840000, "weight_pct": 9.05, "cost_basis": 310.00},
        {"ticker": "XOM", "name": "Exxon Mobil Corporation", "sector": "Energy", "shares": 500000, "price": 108.20, "market_value": 54100000, "weight_pct": 3.38, "cost_basis": 95.00},
        {"ticker": "GLD", "name": "SPDR Gold Shares ETF", "sector": "Commodities", "shares": 600000, "price": 218.50, "market_value": 131100000, "weight_pct": 8.19, "cost_basis": 185.00},
        {"ticker": "TLT", "name": "iShares 20+ Year Treasury ETF", "sector": "Fixed Income", "shares": 800000, "price": 92.30, "market_value": 73840000, "weight_pct": 4.62, "cost_basis": 98.00},
        {"ticker": "SPY", "name": "SPDR S&P 500 ETF", "sector": "Equity ETF", "shares": 350000, "price": 512.80, "market_value": 179480000, "weight_pct": 11.22, "cost_basis": 470.00},
        {"ticker": "CASH", "name": "Cash & Equivalents", "sector": "Cash", "shares": 1, "price": 854070000, "market_value": 854070000, "weight_pct": 34.39, "cost_basis": 854070000},
    ],
    "ALPHA-2": [
        {"ticker": "AAPL", "name": "Apple Inc.", "sector": "Information Technology", "shares": 500000, "price": 228.70, "market_value": 114350000, "weight_pct": 12.44, "cost_basis": 185.00},
        {"ticker": "TSLA", "name": "Tesla Inc.", "sector": "Consumer Discretionary", "shares": 200000, "price": 248.50, "market_value": 49700000, "weight_pct": 5.41, "cost_basis": 200.00},
        {"ticker": "AMD", "name": "Advanced Micro Devices", "sector": "Information Technology", "shares": 300000, "price": 178.20, "market_value": 53460000, "weight_pct": 5.82, "cost_basis": 120.00},
        {"ticker": "CRM", "name": "Salesforce Inc.", "sector": "Information Technology", "shares": 150000, "price": 315.40, "market_value": 47310000, "weight_pct": 5.15, "cost_basis": 260.00},
        {"ticker": "V", "name": "Visa Inc.", "sector": "Financials", "shares": 180000, "price": 290.30, "market_value": 52254000, "weight_pct": 5.69, "cost_basis": 240.00},
        {"ticker": "MA", "name": "Mastercard Inc.", "sector": "Financials", "shares": 100000, "price": 475.80, "market_value": 47580000, "weight_pct": 5.18, "cost_basis": 390.00},
        {"ticker": "NFLX", "name": "Netflix Inc.", "sector": "Communication Services", "shares": 80000, "price": 690.20, "market_value": 55216000, "weight_pct": 6.01, "cost_basis": 500.00},
        {"ticker": "CASH", "name": "Cash & Equivalents", "sector": "Cash", "shares": 1, "price": 499130000, "market_value": 499130000, "weight_pct": 54.30, "cost_basis": 499130000},
    ],
    "MACRO-GLOBAL": [
        {"ticker": "EEM", "name": "iShares MSCI Emerging Markets ETF", "sector": "International Equity", "shares": 1000000, "price": 42.30, "market_value": 42300000, "weight_pct": 7.05, "cost_basis": 38.00},
        {"ticker": "EFA", "name": "iShares MSCI EAFE ETF", "sector": "International Equity", "shares": 800000, "price": 78.50, "market_value": 62800000, "weight_pct": 10.47, "cost_basis": 72.00},
        {"ticker": "GLD", "name": "SPDR Gold Shares ETF", "sector": "Commodities", "shares": 1200000, "price": 218.50, "market_value": 262200000, "weight_pct": 43.70, "cost_basis": 175.00},
        {"ticker": "USO", "name": "United States Oil Fund", "sector": "Commodities", "shares": 500000, "price": 72.40, "market_value": 36200000, "weight_pct": 6.03, "cost_basis": 68.00},
        {"ticker": "TLT", "name": "iShares 20+ Year Treasury ETF", "sector": "Fixed Income", "shares": 600000, "price": 92.30, "market_value": 55380000, "weight_pct": 9.23, "cost_basis": 100.00},
        {"ticker": "UUP", "name": "Invesco DB US Dollar Index ETF", "sector": "Currency", "shares": 1000000, "price": 28.60, "market_value": 28600000, "weight_pct": 4.77, "cost_basis": 27.00},
        {"ticker": "CASH", "name": "Cash & Equivalents", "sector": "Cash", "shares": 1, "price": 112520000, "market_value": 112520000, "weight_pct": 18.75, "cost_basis": 112520000},
    ],
}

DATA_AS_OF = date(2026, 3, 3)
