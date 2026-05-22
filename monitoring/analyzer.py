
import sqlite3
import pandas as pd

conn = sqlite3.connect("database/metrics.db")

df = pd.read_sql_query("SELECT * FROM metrics", conn)

avg_cpu = df["cpu"].mean()
avg_ram = df["ram"].mean()

print("\n=== GreenNode Sustainability Analysis ===")

print(f"Average CPU Usage: {avg_cpu:.2f}%")
print(f"Average RAM Usage: {avg_ram:.2f}%")

if avg_cpu > 70:
    print("Insight: High CPU utilization detected.")
else:
    print("Insight: CPU workload appears efficient.")

if avg_ram > 80:
    print("Insight: High memory pressure detected.")
else:
    print("Insight: Memory usage within efficient range.")
