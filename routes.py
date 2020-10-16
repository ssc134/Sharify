from flask import render_template, redirect, url_for
from main import app
from utils import generate_unique_id

@app.route("/cat")
@app.route("/<string:uid>")
def new_session(uid):
    return f"new **{uid}** session loaded."
    #return render_template("text_editor.html")


@app.route("/")
def homepage():
    uid = generate_unique_id()
    print(uid)
    return redirect(f"/{uid}")
