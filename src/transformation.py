import pandas as pd
import logging

# -------------------------
# FINANCIAL METRICS
# -------------------------
def calculate_financial_metrics(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.copy()

    df["date"] = df["timestamp"].dt.date

    grouped = df.groupby("date").agg(
        total_volume=("amount", "sum"),
        avg_ticket=("amount", "mean"),
        total_transactions=("transaction_id", "count"),
        success_transactions=("status", lambda x: (x == "success").sum())
    ).reset_index()

    grouped["success_rate"] = grouped["success_transactions"] / grouped["total_transactions"]

    logging.info("Financial metrics calculated")

    return grouped


# -------------------------
# USER METRICS
# -------------------------
def calculate_user_metrics(events: pd.DataFrame) -> pd.DataFrame:
    df = events.copy()

    df["date"] = df["timestamp"].dt.date

    daily_active_users = df.groupby("date")["user_id"].nunique().reset_index(name="dau")

    events_per_user = df.groupby("user_id").size().reset_index(name="events_count")

    logging.info("User metrics calculated")

    return daily_active_users, events_per_user


# -------------------------
# COMBINED METRICS
# -------------------------
def calculate_combined_metrics(users, transactions, events):
    # Receita por usuário
    revenue = transactions[transactions["status"] == "success"].groupby("user_id")["amount"].sum().reset_index()
    revenue.rename(columns={"amount": "total_revenue"}, inplace=True)

    user_metrics = users.merge(revenue, on="user_id", how="left")
    user_metrics["total_revenue"] = user_metrics["total_revenue"].fillna(0)

    # Atividade (eventos)
    activity = events.groupby("user_id").size().reset_index(name="total_events")

    user_metrics = user_metrics.merge(activity, on="user_id", how="left")
    user_metrics["total_events"] = user_metrics["total_events"].fillna(0)

    logging.info("Combined metrics calculated")

    return user_metrics


# -------------------------
# ORCHESTRATOR
# -------------------------
def run_transformation(users, transactions, events):
    logging.info("Starting transformation layer...")

    financial_metrics = calculate_financial_metrics(transactions)

    daily_active_users, events_per_user = calculate_user_metrics(events)

    combined_metrics = calculate_combined_metrics(users, transactions, events)

    logging.info("Transformation completed")

    return financial_metrics, daily_active_users, events_per_user, combined_metrics