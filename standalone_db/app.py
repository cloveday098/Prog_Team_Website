from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def home():
    return render_template('dbsignin.html')

@app.route('/login')
def login():
    error = request.args.get('error')
    return render_template('dbsignin.html' , error=error)

@app.route('/process_form', methods=["POST","GET"])
def process_form():

    userid = request.form['userid']
    password = request.form['password']

    # format for the logins is (id, userid, password) as follows:
    # id is an auto-incremented integer primary key,
    # userid is a not null varchar(255) field for a user's username which should be their name
    # password is a not null varchar(255) field
    # for testing, there is a valid username of 'root' and a valid password of 'root' that will result in a log-in
    # users is a table stored in 'logins.db'

    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE userid=? AND password=?" , (userid, password))
    result = cursor.fetchone()

    if result:
        #successfully found the user
        return render_template('home.html')
    else:
        #did not find the user
        return redirect(url_for('login', error='Invalid Login'))

@app.route('/problems')
def problems():
    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems")
    rows = cursor.fetchall()
    return render_template('problems.html', rows=rows)

@app.route('/submitquery', methods=["POST"])
def submitquery():
    query = request.form['query']

    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()

    cursor.execute(query)

    conn.commit()

    cursor.execute("SELECT * FROM problems")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('problems.html' , rows=rows)

@app.route('/editproblem', methods=["POST" , "GET"])
def editproblem():
    problemid = request.args.get("problemid")
    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems where problem_id=?",(problemid))
    rows = cursor.fetchall()

    return render_template('editproblem.html' , rows=rows)

@app.route('/handledeleteproblem')
def handledeleteproblem():
    problemid = request.args.get("problemid")

    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM problems WHERE problem_id = ?", (problemid))
    conn.commit()

    cursor.execute("SELECT * FROM problems")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('problems.html' , rows=rows)

if __name__ == '__main__':
    app.run(debug=True)