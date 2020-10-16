import sqlite3

conn = sqlite3.connect("Available_Ids.db")
c = conn.cursor()
c.execute("SELECT * from Available_Ids")
print(c.fetchall())
conn.close()