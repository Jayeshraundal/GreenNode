
# GreenNode – Sustainable Infrastructure Monitoring

GreenNode is a lightweight Linux infrastructure monitoring platform focused on workload efficiency,
resource utilization, and sustainability-aware infrastructure analysis.

## Features
- Linux CPU and RAM monitoring
- SQLite metric storage
- FastAPI REST API
- Streamlit dashboard
- Docker-ready architecture
- Sustainability-aware workload insights
- AI-ready architecture for future LangChain integration

## Tech Stack
- Python
- FastAPI
- Streamlit
- SQLite
- Docker
- psutil
- pandas

## Run Monitoring Agent
```bash
python monitoring/collector.py
```

## Run API
```bash
uvicorn api.main:app --reload
```

## Run Dashboard
```bash
streamlit run dashboard/dashboard.py
```

## Example Sustainability Insights
- High CPU utilization during low throughput periods
- Idle but resource-intensive workloads
- Resource spikes caused by inefficient scheduling

## Future Improvements
- Docker container monitoring
- Carbon intensity API integration
- LangChain-based AI analysis
- Kubernetes workload support
