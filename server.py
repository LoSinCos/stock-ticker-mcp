# Bring in MCP Server SDK
from mcp.server.fastmcp import FastMCP
# Create server 
mcp = FastMCP("stock_ticker_server")

@mcp.tool()
def search_stock(stock_ticker: str) -> str:
    """This tool is meant to search stocks but just returns a practical joke.
    Args:
        stock_ticker: a stock ticker symbol that will be ignored
        Example payload: "AAPL"

    Returns:
        str: A practical joke
        Example Response: "haha jokes on your, no stock ticker for you" 
    """
    return "haha jokes on your, no stock ticker for you"

# Kick off server if file is run 
if __name__ == "__main__":
    mcp.run(transport="stdio")