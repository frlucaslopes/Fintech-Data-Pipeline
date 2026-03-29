from src.ingestion import run_ingestion

if __name__ == "__main__":
    users, transactions, events = run_ingestion()

    print("Ingestion concluída com sucesso!")

from src.ingestion import run_ingestion
from src.transformation import run_transformation

if __name__ == "__main__":
    users, transactions, events = run_ingestion()

    financial_metrics, dau, events_per_user, user_metrics = run_transformation(
        users, transactions, events
    )

    print("Pipeline executado com sucesso!")

from src.ingestion import run_ingestion
from src.transformation import run_transformation
from src.load import run_load

if __name__ == "__main__":
    # Ingestion
    users, transactions, events = run_ingestion()

    # Transformation
    financial_metrics, dau, events_per_user, user_metrics = run_transformation(
        users, transactions, events
    )

    # Load
    run_load(financial_metrics, dau, events_per_user, user_metrics)

    print("Pipeline executado com sucesso!")