# Industry Demos — Finance

A FastMCP server exposing hedge fund data tools for non-technical users (portfolio managers, risk managers, traders, compliance). Deployed via [Prefect Horizon](https://horizon.prefect.io).

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
| `get_data_freshness` | Last refresh time per data source |

## Funds

- `ALPHA-1` — Benchmark: S&P 500
- `ALPHA-2` — Benchmark: NASDAQ 100
- `MACRO-GLOBAL` — Benchmark: HFRX Global Hedge Fund Index

## Running locally

```bash
pip install -r requirements.txt
fastmcp install claude-code main.py
```

Or run directly:

```bash
fastmcp run main.py
```

## Deploying to Horizon

1. Push this repo to GitHub
2. Visit [horizon.prefect.io](https://horizon.prefect.io) and connect your repo
3. Set entrypoint to `main.py:mcp`
4. Click Deploy — your server will be live at `https://<server-name>.fastmcp.app/mcp`
