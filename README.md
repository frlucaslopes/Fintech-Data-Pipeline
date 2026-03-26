# Fintech-Data-Pipeline
Uma fintech digital que precisa analisar transações e comportamento dos usuários para tomada de decisão.

# 💳 Fintech Data Pipeline — Transaction & User Behavior Analytics
## 📌 Overview

Este projeto simula um cenário real de uma fintech digital, focado na construção de um pipeline de dados completo para análise de:

Transações financeiras
Comportamento dos usuários
Qualidade dos dados

O objetivo é transformar dados brutos em insights acionáveis para tomada de decisão.

## 🎯 Business Problem

Uma fintech precisa responder perguntas críticas como:

Qual o volume financeiro movimentado diariamente?
Qual a taxa de sucesso das transações?
Como os usuários interagem com a plataforma?
Existe relação entre atividade e geração de receita?
🧠 Solution

Construção de um pipeline de dados (ETL) que:

Ingere dados brutos (CSV)
Transforma e calcula métricas de negócio
Entrega datasets prontos para análise
📊 Data Sources

O projeto utiliza 3 fontes principais:

🧑‍💼 Users (users.csv)

Informações de cadastro dos usuários:

Column	Description
user_id	Identificador único
signup_date	Data de cadastro
country	País do usuário
plan	Plano (free / premium)
💳 Transactions (transactions.csv)

Dados de transações financeiras:

Column	Description
transaction_id	ID da transação
user_id	ID do usuário
amount	Valor da transação
transaction_type	Tipo (deposit, withdrawal, payment)
status	Status (success, failed)
timestamp	Data e hora
📲 Events (events.csv)

Eventos de comportamento do usuário:

Column	Description
event_id	ID do evento
user_id	ID do usuário
event_type	Tipo (login, transfer, payment_click)
timestamp	Data e hora
⚙️ Pipeline Architecture

O pipeline segue três etapas principais:

🔹 1. Ingestion
Leitura dos arquivos CSV
Validação de estrutura e schema
Tratamento inicial de dados
🔹 2. Transformation

Cálculo de métricas de negócio:

📈 Financial Metrics
Total Transaction Volume
Average Ticket (Ticket Médio)
Success Rate (% de sucesso)
👤 User Metrics
Daily Active Users (DAU)
Eventos por usuário
Engajamento
🧠 Combined Metrics
Receita por usuário
Relação atividade vs transação
🔹 3. Load
Escrita dos dados transformados em:
daily_metrics.csv
user_metrics.csv
🏗️ Project Structure
fintech-data-pipeline/

├── data/
│   ├── raw/         # Dados brutos
│   ├── processed/   # Dados transformados
│
├── src/
│   ├── ingestion.py
│   ├── transformation.py
│   ├── load.py
│
├── logs/            # Logs de execução
│
├── main.py          # Orquestração do pipeline
├── requirements.txt
├── README.md
└── .github/workflows/ci.yml
