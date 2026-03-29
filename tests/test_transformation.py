import pandas as pd
from src.transformation import calculate_financial_metrics

def test_calculate_financial_metrics():
    # Dados mockados (controlados)
    data = {
        "transaction_id": [1, 2, 3],
        "user_id": [1, 1, 2],
        "amount": [100, 200, 300],
        "transaction_type": ["deposit", "payment", "withdrawal"],
        "status": ["success", "failed", "success"],
        "timestamp": pd.to_datetime([
            "2024-01-01",
            "2024-01-01",
            "2024-01-01"
        ])
    }

    df = pd.DataFrame(data)

    result = calculate_financial_metrics(df)

    # Assertions (regras de negócio)
    assert result["total_volume"].iloc[0] == 600
    assert result["total_transactions"].iloc[0] == 3
    assert result["success_transactions"].iloc[0] == 2
    assert round(result["success_rate"].iloc[0], 2) == 0.67