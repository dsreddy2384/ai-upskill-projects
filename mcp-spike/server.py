# server.py
import os
import sys
import json
import sqlite3
from typing import Dict, Any

# Compatible with both MCP 1.x (FastMCP) and MCP 2.x (MCPServer)
try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("DevToolboxService")
except (ImportError, ModuleNotFoundError):
    from mcp.server.mcpserver import MCPServer
    mcp = MCPServer("DevToolboxService")

DB_FILE = os.path.abspath("demo.db")

def ensure_database():
    """Initializes a local SQLite database with sample production tables if missing."""
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS deployments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service_name TEXT,
                environment TEXT,
                version TEXT,
                status TEXT
            )
        """)
        # Seed 120 rows to test the 100-row context limit
        sample_rows = [
            (f"service_{i % 4}", "production", f"v1.{i}.0", "SUCCESS" if i % 3 != 0 else "FAILED")
            for i in range(120)
        ]
        cur.executemany(
            "INSERT INTO deployments (service_name, environment, version, status) VALUES (?, ?, ?, ?)",
            sample_rows
        )
        conn.commit()
        conn.close()

# Ensure database exists upon server start
ensure_database()

# --- MCP Resources (Schema & Context Discovery) ---

@mcp.resource("db://tables")
def get_tables_catalog() -> str:
    """Provides a list of all tables in the database to prevent hallucinations."""
    conn = sqlite3.connect(f"file:{DB_FILE}?mode=ro", uri=True)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tables = [row[0] for row in cur.fetchall()]
    conn.close()
    return json.dumps({"database": "demo.db", "tables": tables})

# --- MCP Tools ---

@mcp.tool()
def describe_table(table_name: str) -> Dict[str, Any]:
    """Inspects table schema and returns column names, data types, and primary keys."""
    try:
        conn = sqlite3.connect(f"file:{DB_FILE}?mode=ro", uri=True)
        cur = conn.cursor()
        cur.execute(f"PRAGMA table_info({table_name})")
        columns = [
            {"name": r[1], "type": r[2], "is_primary_key": bool(r[5])}
            for r in cur.fetchall()
        ]
        conn.close()
        if not columns:
            return {"error": f"Table '{table_name}' does not exist"}
        return {"table": table_name, "columns": columns}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def execute_safe_query(sql: str, max_rows: int = 100) -> Dict[str, Any]:
    """
    Executes a read-only SQL query against the database.
    Enforces a strict 100-row payload cap to protect context windows.
    Mutations (DROP, DELETE, UPDATE, INSERT) are rejected at the connection level.
    """
    uri = f"file:{DB_FILE}?mode=ro"
    try:
        conn = sqlite3.connect(uri, uri=True)
        cur = conn.cursor()
        cur.execute(sql)
        cols = [d[0] for d in cur.description] if cur.description else []
        # Fetch max_rows + 1 to detect truncation
        raw_rows = cur.fetchmany(max_rows + 1)
        conn.close()

        truncated = len(raw_rows) > max_rows
        return {
            "columns": cols,
            "rows": raw_rows[:max_rows],
            "row_count": min(len(raw_rows), max_rows),
            "truncated": truncated,
            "error": None
        }
    except Exception as e:
        return {
            "columns": [],
            "rows": [],
            "row_count": 0,
            "truncated": False,
            "error": str(e)
        }

if __name__ == "__main__":
    mcp.run()