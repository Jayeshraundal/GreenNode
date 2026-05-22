
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("GreenNode - Sustainable Infrastructure Monitoring")

conn = sqlite3.connect("database/metrics.db")

df = pd.read_sql_query("SELECT * FROM metrics", conn)

if len(df) > 0:
    st.subheader("CPU Utilization")
    cpu_fig = px.line(df, x="timestamp", y="cpu")
    st.plotly_chart(cpu_fig)

    st.subheader("RAM Utilization")
    ram_fig = px.line(df, x="timestamp", y="ram")
    st.plotly_chart(ram_fig)

    avg_cpu = df["cpu"].mean()

    st.subheader("Sustainability Insights")

    if avg_cpu > 70:
        st.warning("High CPU utilization detected. Consider workload optimization.")
    else:
        st.success("System workload appears resource efficient.")
else:
    st.info("No monitoring data available yet.")
