
import psutil
import sqlite3
import time
from datetime import datetime

conn = sqlite3.connect("database/metrics.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS metrics (
    timestamp TEXT,
    cpu REAL,
    ram REAL
)
''')

conn.commit()

print("GreenNode Monitoring Started...")

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO metrics VALUES (?, ?, ?)",
        (timestamp, cpu, ram)
    )

    conn.commit()

    print(f"[{timestamp}] CPU: {cpu}% | RAM: {ram}%")

    time.sleep(5)
