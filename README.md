### MCP playground

as described in https://modelcontextprotocol.io/quickstart/server

#### setupst
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

#### run server
```
uv run weather.py
```