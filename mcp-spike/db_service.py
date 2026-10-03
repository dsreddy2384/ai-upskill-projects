# db_service.py
import os
import sqlite3
from typing import Dict, Any

DB_FILE = "demo.db"

def init_test_db(db_path: str = DB_FILE):
    """Seed a sample database with tables and test rows."""
    if os.path.exists(db_path):
        os.remove(db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE deployments (
            id INTEGER PRIMARY KEY,
            service_name TEXT,
            environment TEXT,
            status TEXT
        )
    """)
    # Seed 150 rows to test our 100-row context limit
    rows = [(f"service_{i % 5}", "production", "SUCCESS" if i % 2 == 0 else "FAILED") for i in range(150)]
    cur.executemany("INSERT INTO deployments (service_name, environment, status) VALUES (?, ?, ?)", rows)
    conn.commit()
    conn.close()

def describe_table(table_name: str, db_path: str = DB_FILE) -> Dict[str, Any]:
    """Exposes table schema metadata to prevent hallucinated columns."""
    try:
        conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        cur = conn.cursor()
        cur.execute(f"PRAGMA table_info({table_name})")
        columns = [{"name": row[1], "type": row[2], "is_primary_key": bool(row[5])} for row in cur.fetchall()]
        conn.close()
        if not columns:
            return {"error": f"Table '{table_name}' does not exist"}
        return {"table": table_name, "columns": columns}
    except Exception as e:
        return {"error": str(e)}

def execute_safe_query(sql: str, db_path: str = DB_FILE, max_rows: int = 100) -> Dict[str, Any]:
    """Executes SQL with read-only connection guarantees and hard payload caps."""
    uri = f"file:{db_path}?mode=ro"
    try:
        conn = sqlite3.connect(uri, uri=True)
        cur = conn.cursor()
        cur.execute(sql)
        cols = [d[0] for d in cur.description] if cur.description else []
        # Fetch up to max_rows + 1 to detect truncation
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