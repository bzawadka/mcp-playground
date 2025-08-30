## MCP playground

as described in https://modelcontextprotocol.io/quickstart/server

### setupst
providing `uv` is installed:

```
# Create a new directory for our project
uv init weather
cd weather

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx

# Create our server file
touch weather.py
```

### run server
```
uv run weather.py
```

### configure with Claude Desktop
1. open `%APPDATA%\Claude\claude_desktop_config.json`
1. add configuration for this MCP server
```
{
    "mcpServers": {
        "weather": {
            "command": "C:\\Users\\dafi\\.local\\bin\\uv",
            "args": [
                "--directory",
                "C:\\Users\\dafi\\workspace\\mcp-playground",
                "run",
                "weather.py"
            ]
        }
    }
}
```
