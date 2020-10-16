from flask import Flask, render_template, redirect, url_for
import sqlite3

"""
 Unique_Ids.db has 2 tables named 'Used' and 'Unused'.
 Tables 'Used' & 'Unused' have a common attribute 'id'.
"""


app = Flask(__name__)


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


@app.route("/cat")
@app.route("/<string:uid>")
def session(uid):
    return f"{uid} session loaded"


@app.route("/")
def homepage():
    uid = generate_unique_id()
    print(uid)
    return redirect(f"/{uid}")


if __name__ == "__main__":
    app.run(debug=True)