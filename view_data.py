import sqlite3

conn = sqlite3.connect("records")
cur = conn.cursor()

cur.execute("SELECT * FROM usr_data;")
print(cur.fetchall())