# Stock Ticker MCP Server

[![smithery badge](https://smithery.ai/badge/@LoSinCos/stock-ticker-mcp)](https://smithery.ai/server/@LoSinCos/stock-ticker-mcp)

A simple MCP server that responds with a rude message when queried about stocks. This is a demo implementation of the Model Context Protocol (MCP).

## Features

- Single tool: `search_stock` that returns a rude message
- Compatible with Claude Desktop

## Installation

### Installing via Smithery

To install Stock Ticker Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@LoSinCos/stock-ticker-mcp):

```bash
npx -y @smithery/cli install @LoSinCos/stock-ticker-mcp --client claude
```

### Manual Installation
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

## Usage with Claude Desktop

1. Add the server configuration to your Claude Desktop config:

```json
{
  "mcpServers": {
    "stock_ticker_server": {
      "command": "uv",
      "args": ["--directory", "/path/to/stock-ticker-mcp", "run", "server.py"]
    }
  }
}
```

2. Restart Claude Desktop
3. Look for the hammer icon to access the tool
