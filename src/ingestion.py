import pandas as pd
import logging
import os

# -------------------------
# PATHS
# -------------------------
RAW_PATH = "data/raw"
SILVER_PATH = "data/silver"

os.makedirs("logs", exist_ok=True)
os.makedirs(SILVER_PATH, exist_ok=True)

# -------------------------
# LOGGING CONFIG
# -------------------------
logging.basicConfig(
    filename="logs/ingestion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------
# SCHEMA DEFINITIONS
# -------------------------
USERS_SCHEMA = {
    "user_id": "int64",
    "signup_date": "datetime64[ns]",
    "country": "object",
    "plan": "object"
}

TRANSACTIONS_SCHEMA = {
    "transaction_id": "int64",
    "user_id": "int64",
    "amount": "float64",
    "transaction_type": "object",
    "status": "object",
    "timestamp": "datetime64[ns]"
}

EVENTS_SCHEMA = {
    "event_id": "int64",
    "user_id": "int64",
    "event_type": "object",
    "timestamp": "datetime64[ns]"
}

# -------------------------
# GENERIC FUNCTIONS
# -------------------------
def read_csv(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Loaded file: {file_path} | Rows: {len(df)}")
        return df
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
        raise


def validate_columns(df: pd.DataFrame, expected_columns: dict, dataset_name: str):
    missing_cols = set(expected_columns.keys()) - set(df.columns)
    
    if missing_cols:
        error_msg = f"{dataset_name} missing columns: {missing_cols}"
        logging.error(error_msg)
        raise ValueError(error_msg)
    
    logging.info(f"{dataset_name} columns validated")


def cast_types(df: pd.DataFrame, schema: dict, dataset_name: str) -> pd.DataFrame:
    for col, dtype in schema.items():
        try:
            if "datetime" in dtype:
                df[col] = pd.to_datetime(df[col], errors="coerce")
            else:
                df[col] = df[col].astype(dtype)
        except Exception as e:
            logging.warning(f"{dataset_name} - Error casting {col}: {e}")

    logging.info(f"{dataset_name} types casted")
    return df


def basic_data_quality_checks(df: pd.DataFrame, dataset_name: str):
    nulls = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    logging.info(f"{dataset_name} null values: {nulls}")
    logging.info(f"{dataset_name} duplicate rows: {duplicates}")


# -------------------------
# SILVER SAVE FUNCTION (NOVO)
# -------------------------
def save_silver(df: pd.DataFrame, filename: str):
    path = os.path.join(SILVER_PATH, filename)
    try:
        df.to_csv(path, index=False)
        logging.info(f"Saved SILVER file: {path} | Rows: {len(df)}")
    except Exception as e:
        logging.error(f"Error saving SILVER file {path}: {e}")
        raise


# -------------------------
# MAIN INGESTION FUNCTIONS
# -------------------------
def load_users():
    df = read_csv(os.path.join(RAW_PATH, "users.csv"))
    validate_columns(df, USERS_SCHEMA, "users")
    df = cast_types(df, USERS_SCHEMA, "users")
    basic_data_quality_checks(df, "users")

    save_silver(df, "users_clean.csv")  # NOVO

    return df


def load_transactions():
    df = read_csv(os.path.join(RAW_PATH, "transactions.csv"))
    validate_columns(df, TRANSACTIONS_SCHEMA, "transactions")
    df = cast_types(df, TRANSACTIONS_SCHEMA, "transactions")
    basic_data_quality_checks(df, "transactions")

    save_silver(df, "transactions_clean.csv")  # NOVO

    return df


def load_events():
    df = read_csv(os.path.join(RAW_PATH, "events.csv"))
    validate_columns(df, EVENTS_SCHEMA, "events")
    df = cast_types(df, EVENTS_SCHEMA, "events")
    basic_data_quality_checks(df, "events")

    save_silver(df, "events_clean.csv")  # NOVO

    return df


# -------------------------
# ORCHESTRATOR
# -------------------------
def run_ingestion():
    logging.info("Starting ingestion pipeline...")

    users = load_users()
    transactions = load_transactions()
    events = load_events()

    logging.info("Ingestion pipeline completed successfully")

    return users, transactions, events