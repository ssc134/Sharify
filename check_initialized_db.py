import sqlite3

connection = sqlite3.connect("Unique_Ids.db")
cur = connection.cursor()
cur.execute("SELECT * from Used LIMIT 5")
print(cur.fetchall())
cur.execute("SELECT * from Unused LIMIT 5")
print(cur.fetchall())
connection.close()
