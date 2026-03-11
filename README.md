# Industry Demos — Hedge Fund

A FastMCP server exposing hedge fund data tools for portfolio managers, risk managers, traders, and compliance officers. Deployed via [Prefect Horizon](https://horizon.prefect.io).

## Tools

| Tool | Description |
|------|-------------|
| `get_portfolio_holdings` | Current positions, weights, and unrealized P&L |
| `get_sector_exposure` | Portfolio breakdown by sector |
| `get_fund_performance` | Fund vs benchmark returns for any period |
| `get_performance_attribution` | Which positions drove returns |
| `get_risk_metrics` | VaR, volatility, Sharpe, Sortino, max drawdown |
| `get_factor_exposures` | Beta, momentum, value, quality factor tilts |
| `get_liquidity_analysis` | Days to unwind each position at 20% ADV |
| `get_trade_blotter` | Executed trades, filterable by fund and date |
| `check_risk_limits` | Compliance check against configurable risk limits |
| `get_data_freshness` | Last refresh time per data source |

## Funds

- `ALPHA-1` — $1.6B NAV, long/short equity, Benchmark: S&P 500
- `ALPHA-2` — $919M NAV, tech-focused growth, Benchmark: NASDAQ 100
- `MACRO-GLOBAL` — $600M NAV, global macro, Benchmark: HFRX Global Hedge Fund Index

## Live Demo: Change Code, Watch Agent Respond

The `RISK_LIMITS` dict at the top of `main.py` controls compliance thresholds:

```python
RISK_LIMITS = {
    "max_position_pct": 15,       # max single-position weight (%)
    "max_sector_pct": 40,         # max single-sector weight (%)
    "max_var_95_pct": 2.0,        # max daily VaR at 95% as % of NAV
    "min_liquidity_1d_pct": 50,   # min % of portfolio liquidatable in 1 day
}
```

**Demo flow:**

1. Ask: *"Is MACRO-GLOBAL in compliance?"*
   - Agent calls `check_risk_limits` → **BREACH** (GLD is 43.7% of the portfolio, limit is 15%)
2. Open `main.py`, change `max_position_pct` from `15` to `50`
3. Push to GitHub → Horizon redeploys automatically
4. Ask the same question again → **PASS**

This shows how Horizon keeps the agent in sync with code changes in real time.

## Running locally

```bash
pip install -r requirements.txt
fastmcp run main.py
```

## Deploying to Horizon

1. Push this repo to GitHub
2. Visit [horizon.prefect.io](https://horizon.prefect.io) and connect your repo
3. Set entrypoint to `main.py:mcp`
4. Click Deploy — your server will be live at `https://<server-name>.fastmcp.app/mcp`
