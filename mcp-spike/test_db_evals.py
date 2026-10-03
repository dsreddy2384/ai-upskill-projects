# test_db_evals.py
import pytest
from db_service import init_test_db, execute_safe_query, describe_table, DB_FILE

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Ensure test database is initialized before any tests run."""
    init_test_db(DB_FILE)

def test_read_only_connection_blocks_mutations():
    """Decision 1: Connection-level read-only guarantees must reject writes."""
    res = execute_safe_query("DELETE FROM deployments WHERE id = 1")
    assert res["error"] is not None
    assert "readonly" in res["error"].lower()

def test_large_query_is_capped_at_100_rows():
    """Decision 2: Results exceeding 100 rows must be truncated to protect context."""
    res = execute_safe_query("SELECT * FROM deployments")
    assert res["error"] is None
    assert res["row_count"] == 100
    assert len(res["rows"]) == 100
    assert res["truncated"] is True

def test_small_query_returns_full_dataset():
    """Decision 2: Sub-100 queries must not trigger truncation."""
    res = execute_safe_query("SELECT * FROM deployments WHERE id <= 10")
    assert res["error"] is None
    assert res["row_count"] == 10
    assert res["truncated"] is False

def test_schema_discovery_returns_exact_columns():
    """Decision 4: describe_table must return valid column names to ground the LLM."""
    metadata = describe_table("deployments")
    assert "error" not in metadata
    col_names = [col["name"] for col in metadata["columns"]]
    assert "service_name" in col_names
    assert "environment" in col_names
    assert "status" in col_names

def test_syntax_error_returns_actionable_message():
    """Decision 5: Raw error messages must be preserved so the LLM can self-correct."""
    res = execute_safe_query("SELECT non_existent_column FROM deployments")
    assert res["error"] is not None
    assert "no such column" in res["error"].lower()