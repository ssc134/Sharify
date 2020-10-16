import sqlite3

# Create a database named Unavailable_ids.db
# and create a table in it named Unavailable_Ids
# Then close the connection
conn = sqlite3.connect("Unavailable_Ids.db")
c = conn.cursor()
c.execute("CREATE TABLE Unavailable_Ids (unique_name TEXT NOT NULL PRIMARY KEY)")
conn.commit()
conn.close()

# Create a database named Available_ids.db
# and create a table in it named Available_Ids.
# Then copy ids from file docker_names.txt from folder generate_docker_names
# and insert into Available_ids.db.
# Lastly close the file and close the db connection.
conn = sqlite3.connect("Available_Ids.db")
c = conn.cursor()
file = open("generate_docker_names/docker_names.txt")
c.execute("CREATE TABLE Available_Ids (unique_name TEXT NOT NULL PRIMARY KEY )")
for line in file:
    c.execute(f"INSERT INTO Available_Ids VALUES ('{line}')")
conn.commit()
file.close()
conn.close()