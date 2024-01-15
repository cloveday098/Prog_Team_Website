from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    # format for the logins is (id, userid, password) as follows:
    # id is an auto-incremented integer primary key,
    # userid is a not null varchar(255) field for a user's username which should be their name
    # password is a not null varchar(255) field
    conn = sqlite3.connect('logins.db')

    cursor = conn.cursor()

    # Do DB interactions here

    conn.commit()
    conn.close()

    return render_template('dbsignin.html')

if __name__ == '__main__':
    app.run(debug=True)