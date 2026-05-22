
from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI(title="GreenNode API")

@app.get("/metrics")
def get_metrics():
    conn = sqlite3.connect("database/metrics.db")
    df = pd.read_sql_query("SELECT * FROM metrics", conn)

    return df.tail(20).to_dict(orient="records")
