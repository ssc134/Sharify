from flask import Flask

"""
 Unique_Ids.db has 2 tables named 'Used' and 'Unused'.
 Tables 'Used' & 'Unused' have a common attribute 'id'.
"""


app = Flask(__name__)

from routes import *

if __name__ == "__main__":
    app.run(debug=True)