from flask import Flask, render_template, redirect, url_for
import sqlite3

available_id_connection = sqlite3.connect("Available_Ids.db")
available_id_cursor = available_id_connection.cursor()

unavailable_id_connection = sqlite3.connect("Unavailable_Ids.db")
unavailable_id_cursor = unavailable_id_connection.cursor()


app = Flask(__name__)

@app.route('/cat')
def session():
    return "hello world"

@app.route('/')
def homepage():
    
    return redirect("/cat")

if __name__=='__main__':
    app.run(debug=True)