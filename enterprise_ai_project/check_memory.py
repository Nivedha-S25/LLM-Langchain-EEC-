import sqlite3

conn = sqlite3.connect("data/processed/enterprise_intelligence.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM decision_memory")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
