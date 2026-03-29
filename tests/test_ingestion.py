import pandas as pd
import pytest
from src.ingestion import validate_columns


def test_validate_columns_success():
    df = pd.DataFrame({
        "user_id": [1],
        "signup_date": ["2024-01-01"],
        "country": ["BR"],
        "plan": ["free"]
    })

    schema = {
        "user_id": "int64",
        "signup_date": "datetime64[ns]",
        "country": "object",
        "plan": "object"
    }

    # Não deve lançar erro
    validate_columns(df, schema, "users")


def test_validate_columns_failure():
    df = pd.DataFrame({
        "user_id": [1]
    })

    schema = {
        "user_id": "int64",
        "signup_date": "datetime64[ns]"
    }

    with pytest.raises(ValueError):
        validate_columns(df, schema, "users")