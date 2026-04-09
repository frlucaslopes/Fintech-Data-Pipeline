import pandas as pd
import streamlit as st

st.set_page_config(page_title="Fintech Dashboard", layout="wide")

st.title("💳 Fintech Data Pipeline Dashboard")

# -------------------------
# LOAD DATA
# -------------------------
daily_metrics = pd.read_csv("data/processed/daily_metrics.csv")
user_metrics = pd.read_csv("data/processed/user_metrics.csv")
revenue_per_user = pd.read_csv("data/processed/revenue_per_user.csv")

# Para análises mais avançadas
transactions = pd.read_csv("data/raw/transactions.csv")

# -------------------------
# FILTER
# -------------------------
st.sidebar.header("Filtros")

daily_metrics['date'] = pd.to_datetime(daily_metrics['date'])

data_min = daily_metrics['date'].min()
data_max = daily_metrics['date'].max()

data_range = st.sidebar.date_input(
    "Selecione o período",
    [data_min, data_max]
)

daily_metrics = daily_metrics[
    (daily_metrics['date'] >= pd.to_datetime(data_range[0])) &
    (daily_metrics['date'] <= pd.to_datetime(data_range[1]))
]

# -------------------------
# FINANCIAL + MONETIZATION KPIs
# -------------------------
st.subheader("📈 Visão Geral do Negócio")

col1, col2, col3, col4 = st.columns(4)

total_volume = daily_metrics['total_volume'].sum()
avg_ticket = daily_metrics['avg_ticket'].mean()
success_rate = daily_metrics['success_rate'].mean()

total_revenue = revenue_per_user["revenue"].sum()
arpu = revenue_per_user["revenue"].mean()

col1.metric("💰 Volume Total", f"R$ {total_volume:,.2f}")
col2.metric("📊 Ticket Médio", f"R$ {avg_ticket:,.2f}")
col3.metric("✅ Taxa de Sucesso", f"{success_rate:.2%}")
col4.metric("💵 ARPU", f"R$ {arpu:,.2f}")

# -------------------------
# BUSINESS INSIGHT
# -------------------------
st.subheader("🧠 Insight de Negócio")

if arpu > 50:
    st.success("ARPU elevado — forte monetização por usuário.")
else:
    st.warning("ARPU baixo — oportunidade de aumentar monetização.")

if success_rate < 0.9:
    st.warning("Taxa de sucesso abaixo do ideal. Possíveis falhas operacionais.")
else:
    st.success("Operação estável com alta taxa de sucesso.")

# -------------------------
# REVENUE OVER TIME (NOVO)
# -------------------------
st.subheader("📊 Receita ao longo do tempo")

transactions = transactions[transactions["status"] == "success"]
transactions["timestamp"] = pd.to_datetime(transactions["timestamp"])
transactions["date"] = transactions["timestamp"].dt.date

revenue_daily = transactions.groupby("date")["amount"].sum()

st.line_chart(revenue_daily)

# -------------------------
# TOP USERS
# -------------------------
st.subheader("🏆 Top Usuários por Receita")

top_users = revenue_per_user.sort_values(by="revenue", ascending=False).head(10)
st.dataframe(top_users)

# -------------------------
# REVENUE BY PLAN (NOVO)
# -------------------------
st.subheader("💳 Receita por Tipo de Plano")

merged = user_metrics.merge(revenue_per_user, on="user_id", how="left")
merged["revenue"] = merged["revenue"].fillna(0)

revenue_by_plan = merged.groupby("plan")["revenue"].mean()

st.bar_chart(revenue_by_plan)

# -------------------------
# USER DATA
# -------------------------
st.subheader("👤 Métricas de Usuário")
st.dataframe(user_metrics.head())