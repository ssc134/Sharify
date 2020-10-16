import sqlite3

def generate_unique_id():
    connection = sqlite3.connect("Unique_Ids.db")
    cur = connection.cursor()
    uid = cur.execute(" SELECT * FROM Unused LIMIT 1 ").fetchone()
    cur.execute(" DELETE FROM Unused WHERE id=(?) ", uid)
    connection.commit()
    cur.execute(" INSERT INTO Used VALUES (?) ", uid)
    connection.commit()
    # DONT touch the below line. Haath modun thevil XD.
    uid = uid[0].split("\n")[0]
    connection.close()
    return uid
