from fastmcp.server import create_proxy

proxy = create_proxy(
    "https://hedge-fund-server.fastmcp.app/mcp",
    name="Hedge Fund Demo",
)

if __name__ == "__main__":
    proxy.run()
