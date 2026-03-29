import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Criar pasta se não existir
os.makedirs("data/raw", exist_ok=True)

np.random.seed(42)

# -------------------------
# CONFIG
# -------------------------
NUM_USERS = 1000
NUM_TRANSACTIONS = 15000
NUM_EVENTS = 30000

START_DATE = datetime.now() - timedelta(days=90)

# -------------------------
# USERS
# -------------------------
users = pd.DataFrame({
    "user_id": range(1, NUM_USERS + 1),
    "signup_date": [
        START_DATE + timedelta(days=random.randint(0, 90))
        for _ in range(NUM_USERS)
    ],
    "country": np.random.choice(["BR", "US", "UK", "DE"], NUM_USERS, p=[0.6, 0.2, 0.1, 0.1]),
    "plan": np.random.choice(["free", "premium"], NUM_USERS, p=[0.7, 0.3])
})

users.to_csv("data/raw/users.csv", index=False)

# -------------------------
# TRANSACTIONS
# -------------------------
transactions = pd.DataFrame({
    "transaction_id": range(1, NUM_TRANSACTIONS + 1),
    "user_id": np.random.choice(users["user_id"], NUM_TRANSACTIONS),
    "amount": np.round(np.random.exponential(scale=100), 2),
    "transaction_type": np.random.choice(
        ["deposit", "withdrawal", "payment"],
        NUM_TRANSACTIONS,
        p=[0.4, 0.3, 0.3]
    ),
    "status": np.random.choice(
        ["success", "failed"],
        NUM_TRANSACTIONS,
        p=[0.9, 0.1]
    ),
    "timestamp": [
        START_DATE + timedelta(days=random.randint(0, 90),
                               seconds=random.randint(0, 86400))
        for _ in range(NUM_TRANSACTIONS)
    ]
})

transactions.to_csv("data/raw/transactions.csv", index=False)

# -------------------------
# EVENTS
# -------------------------
events = pd.DataFrame({
    "event_id": range(1, NUM_EVENTS + 1),
    "user_id": np.random.choice(users["user_id"], NUM_EVENTS),
    "event_type": np.random.choice(
        ["login", "transfer", "payment_click"],
        NUM_EVENTS,
        p=[0.5, 0.3, 0.2]
    ),
    "timestamp": [
        START_DATE + timedelta(days=random.randint(0, 90),
                               seconds=random.randint(0, 86400))
        for _ in range(NUM_EVENTS)
    ]
})

events.to_csv("data/raw/events.csv", index=False)

print("✅ Dados gerados com sucesso em data/raw/")