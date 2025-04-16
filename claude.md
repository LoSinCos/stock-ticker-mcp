# Claude Integration Guide

This MCP server provides a single tool:

## Tools

### search_stock

Returns a rude message when queried about any stock.

**Input**:

- stock_ticker (string): A stock ticker symbol (e.g., "AAPL")

**Output**:

- Returns: A rude message

**Example**:

```python
Input: "AAPL"
Output: "haha this is a practical joke"
```

## Configuration

Add this server to your Claude Desktop configuration at `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "stock_ticker_server": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/stock-ticker-mcp",
        "run",
        "server.py"
      ]
    }
  }
}
```

````

4. Create a `LICENSE` (using MIT License):
```markdown
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions...
[rest of MIT license text]
````

5. Your `server.py` remains the same:

```python
from mcp.server.fastmcp import FastMCP

# Create server
mcp = FastMCP("stock_ticker_server")

@mcp.tool()
def search_stock(stock_ticker: str) -> str:
    """This tool is meant to search stocks but just returns a rude message.
    Args:
        stock_ticker: a stock ticker symbol that will be ignored
        Example payload: "AAPL"

    Returns:
        str: A rude message
        Example Response: "fuck you"
    """
    return "fuck you"

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

6. Create a `.gitignore`:
