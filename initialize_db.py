import sqlite3

# Create and establish a connection with database Unique_Ids.db
connection = sqlite3.connect("Unique_Ids.db")

# Get cursor for the connection
cur = connection.cursor()

# Create a table named 'Used' for used ids.
cur.execute("CREATE TABLE Used (id TEXT NOT NULL PRIMARY KEY)")

# Create a table named 'Unused' for unused ids.
cur.execute("CREATE TABLE Unused (id TEXT NOT NULL PRIMARY KEY)")

# Initialized the table 'Unused' with all the names.
# Open file containing unique names and insert the names into table 'Unused'
file = open("docker_names/unique_names.txt")
for line in file:
    cur.execute(f"INSERT INTO Unused VALUES ('{line}') ")

# Commit to the database
connection.commit()

# Lastly close the file & the connection to the database.
file.close()
connection.close()
