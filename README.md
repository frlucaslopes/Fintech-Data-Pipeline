# Fintech Data Pipeline — Transaction & User Behavior Analytics (Análise de transações e comportamento do usuário)

## Overview (Visão Geral)

Este projeto simula um ambiente real de uma **fintech digital**, com foco na construção de um pipeline de dados completo para análise de:

* Transações financeiras
* Comportamento de usuários
* Performance operacional

O pipeline transforma dados brutos em **métricas estratégicas prontas para tomada de decisão**.

---

## Business Problem (Problemática)

Uma fintech precisa responder:

* Quanto dinheiro está sendo movimentado diariamente?
* Qual a eficiência das transações (taxa de sucesso)?
* Usuários ativos geram mais receita?
* Existe relação entre comportamento e monetização?

---

## Solution (Solução)

Desenvolvimento de um pipeline ETL com:

* Ingestão de dados brutos (CSV)
* Validação e tratamento
* Cálculo de métricas de negócio
* Geração de datasets analíticos

---

## Data Architecture (Medallion Architecture)

O projeto segue o conceito de camadas:

### Bronze — Raw Data (Dados Brutos)

📁 `data/raw/`

* Dados brutos
* Sem tratamento
* Origem do sistema

---

### Silver — Clean Data (Dados Limpos)

(Em memória — etapa de transformação)

* Tipagem corrigida
* Dados validados
* Base confiável

---

### Gold — Analytics Layer (Camada Analítica)

📁 `data/processed/`

* Dados agregados
* Métricas de negócio
* Prontos para BI

---

## Data Sources (Fontes de Dados)

### Users (Usuários)

Informações cadastrais dos usuários

### Transactions (Transações)

Registros financeiros

### Events (Eventos)

Interações do usuário com a plataforma

---

## Pipeline Flow (Fluxo)

```text
Raw Data → Ingestion → Validation → Transformation → Metrics → Load
```

---

## Key Metrics (Métricas-Chave)

### Financial Metrics (Métricas Financeiras)

* Total Transaction Volume (Volume total de transações)
* Average Ticket (Ticket Médio)
* Success Rate (Taxa de Sucesso)

### User Metrics (Métricas do Usuário)

* Daily Active Users (DAU) - Usuários ativos diários (UAD)
* Events per User (Eventos por Usuário)

### Business Metrics (Métricas de Negócio)

* Revenue per User (Receita por Usuário)
* Engagement vs Monetization (Engajamento vs Monetização)

---

## Sample Insights (Simulated) - Exemplos de Insights (Simulados)

>  Dados simulados para fins educacionais

* 📈 Usuários **premium geram mais receita média**
* 🔄 Taxa de sucesso média ~90%, indicando estabilidade operacional
* 📊 Usuários mais ativos apresentam maior volume de transações
* 📉 Eventos de login têm forte correlação com pagamentos

---

## Project Structure (Estrutura do Projeto)

```
fintech-data-pipeline/

├── data/
│   ├── raw/
│   ├── processed/
│
├── src/
│   ├── ingestion.py
│   ├── transformation.py
│   ├── load.py
│
├── logs/
├── main.py
├── requirements.txt
└── README.md
```

---

## How to Run

```bash
git clone https://github.com/frlucaslopes/fintech-data-pipeline.git
cd fintech-data-pipeline
pip install -r requirements.txt
python main.py
```

---

## Outputs

* `daily_metrics.csv`
* `user_metrics.csv`
* `daily_active_users.csv`
* `events_per_user.csv`

---

## Future Improvements (Melhorias Futuras)

* [ ] Criar camada Silver persistida
* [ ] Integração com PostgreSQL
* [ ] Orquestração com Airflow
* [ ] Testes automatizados (Pytest)
* [ ] Dashboard (Power BI / Streamlit)
* [ ] Data Quality Framework

---

## What This Project Demonstrates (O que este projeto demonstra)

* ✔ Pipeline de dados end-to-end
* ✔ Pensamento orientado a negócio
* ✔ Organização de código profissional
* ✔ Modelagem de métricas reais
* ✔ Base para arquitetura de dados moderna

---

## Author (Autor)

Lucas M. Lopes - Data Engineer (Engenheiro de Dados)

---

## 📄 License (Licença)

Projeto para fins educacionais e portfólio.


