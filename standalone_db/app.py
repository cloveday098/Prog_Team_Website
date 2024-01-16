from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dbsignin.html')

@app.route('/process_form', methods=["POST"])
def process_form():

    userid = request.form['userid']
    password = request.form['password']

    # format for the logins is (id, userid, password) as follows:
    # id is an auto-incremented integer primary key,
    # userid is a not null varchar(255) field for a user's username which should be their name
    # password is a not null varchar(255) field
    conn = sqlite3.connect('logins.db')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE userid=? AND password=?" , (userid, password))
    result = cursor.fetchone()

    if result:
        #successfully found the user
        return "successfully logged in!"
    else:
        #did not find the user
        return "failed log in!"

    conn.close()

if __name__ == '__main__':
    app.run(debug=True)