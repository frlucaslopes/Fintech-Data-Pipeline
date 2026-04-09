from src.ingestion import run_ingestion
from src.transformation import run_transformation
from src.load import run_load
import src.transformation as t
print("USANDO ARQUIVO:", t.__file__)

if __name__ == "__main__":
    # -------------------------
    # INGESTION
    # -------------------------
    users, transactions, events = run_ingestion()

    # -------------------------
    # TRANSFORMATION
    # -------------------------
    financial_metrics, dau, events_per_user, user_metrics, revenue_per_user = run_transformation(
        users, transactions, events
    )

    # -------------------------
    # LOAD
    # -------------------------
    run_load(
        financial_metrics,
        dau,
        events_per_user,
        user_metrics,
        revenue_per_user  # novo parâmetro
    )

    print("Pipeline executado com sucesso!")
    