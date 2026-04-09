import os
import pandas as pd
import logging

# -------------------------
# CONFIG
# -------------------------
OUTPUT_PATH = "data/processed"

os.makedirs(OUTPUT_PATH, exist_ok=True)

# -------------------------
# GENERIC SAVE FUNCTION
# -------------------------
def save_dataframe(df: pd.DataFrame, filename: str):
    file_path = os.path.join(OUTPUT_PATH, filename)
    
    try:
        df.to_csv(file_path, index=False)
        logging.info(f"Saved file: {file_path} | Rows: {len(df)}")
    except Exception as e:
        logging.error(f"Error saving {file_path}: {e}")
        raise


# -------------------------
# LOAD FUNCTIONS
# -------------------------
def save_financial_metrics(financial_metrics: pd.DataFrame):
    save_dataframe(financial_metrics, "daily_metrics.csv")


def save_user_metrics(user_metrics: pd.DataFrame):
    save_dataframe(user_metrics, "user_metrics.csv")


def save_dau(dau: pd.DataFrame):
    save_dataframe(dau, "daily_active_users.csv")


def save_events_per_user(events_per_user: pd.DataFrame):
    save_dataframe(events_per_user, "events_per_user.csv")

def save_revenue_per_user(revenue_per_user: pd.DataFrame):
    save_dataframe(revenue_per_user, "revenue_per_user.csv")
print("SALVANDO REVENUE PER USER...")
# -------------------------
# ORCHESTRATOR
# -------------------------
def run_load(financial_metrics, dau, events_per_user, user_metrics, revenue_per_user):
    logging.info("Starting load layer...")

    save_financial_metrics(financial_metrics)
    save_user_metrics(user_metrics)
    save_dau(dau)
    save_events_per_user(events_per_user)
    save_revenue_per_user(revenue_per_user)

    logging.info("Load layer completed successfully")
    