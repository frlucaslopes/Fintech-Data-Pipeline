import pandas as pd
import streamlit as st

st.set_page_config(page_title="Fintech Dashboard", layout="wide")

st.title("💳 Fintech Data Pipeline Dashboard")

# Load data
daily_metrics = pd.read_csv("data/processed/daily_metrics.csv")
user_metrics = pd.read_csv("data/processed/user_metrics.csv")

# 🔥 FILTRO (entra AQUI)
st.sidebar.header("Filtros")

daily_metrics['date'] = pd.to_datetime(daily_metrics['date'])

data_min = daily_metrics['date'].min()
data_max = daily_metrics['date'].max()

data_range = st.sidebar.date_input(
    "Selecione o período",
    [data_min, data_max]
)

# Aplicando filtro
daily_metrics = daily_metrics[
    (daily_metrics['date'] >= pd.to_datetime(data_range[0])) &
    (daily_metrics['date'] <= pd.to_datetime(data_range[1]))
]

# KPIs
st.subheader("📈 Métricas Financeiras")
col1, col2, col3 = st.columns(3)

total_volume = daily_metrics['total_volume'].sum()
avg_ticket = daily_metrics['avg_ticket'].mean()
success_rate = daily_metrics['success_rate'].mean()

col1.metric("💰 Volume Total", f"R$ {total_volume:,.2f}")
col2.metric("📊 Ticket Médio", f"R$ {avg_ticket:,.2f}")
col3.metric("✅ Taxa de Sucesso", f"{success_rate:.2%}")

# Insight
st.subheader("🧠 Insight")

if success_rate < 0.9:
    st.warning("Taxa de sucesso abaixo do ideal. Verificar falhas nas transações.")
else:
    st.success("Taxa de sucesso saudável.")

# Chart
st.subheader("📊 Volume ao longo do tempo")
st.line_chart(
    daily_metrics.set_index("date")[["total_volume", "avg_ticket"]]
)

# Users
st.subheader("👤 Métricas de Usuário")
st.dataframe(user_metrics.head())