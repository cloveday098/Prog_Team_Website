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

    # EXTENSIVE USER VALIDATION NEEDED HERE
    # 
    # 

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

@app.route('/categories')
def categories():
    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    rows = cursor.fetchall()
    return render_template('categories.html', rows=rows)

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

    cursor.execute("SELECT * FROM problems where problem_id=?", ((problemid,)))
    rows = cursor.fetchall()

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    return render_template('editproblem.html' , rows=rows, pid=problemid, categories=categories)

@app.route('/editcategory', methods=["POST" , "GET"])
def editcategory():
    categoryid = request.args.get("categoryid")
    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM categories where category_id=?" , (categoryid,))
    rows = cursor.fetchall()

    return render_template('editcategory.html' , rows=rows, cid=categoryid)

@app.route('/handledeleteproblem')
def handledeleteproblem():
    problemid = request.args.get("problemid")

    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM problems WHERE problem_id = ?", ((problemid,)))
    conn.commit()

    cursor.execute("SELECT * FROM problems")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('problems.html' , rows=rows)

@app.route('/handledeletecategory')
def handledeletecategory():
    categoryid = request.args.get("categoryid")
    print(categoryid)

    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM categories WHERE category_id = ?" , (categoryid,))
    conn.commit()

    cursor.execute("SELECT * FROM categories")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('categories.html' , rows=rows)

@app.route('/submitedit', methods=["POST","GET"])
def submitedit():
    # EXTENSIVE VALIDATION GOES HERE
    #
    # 

    # TWO CATEGORY VARIABLES: category IS THE ID, IT IS FUNCTIONAL. actualcategories IS AN ATTEMPTED LIST OF CATEGORY NAMES, BUT IT IS NOT FUNCTIONAL RIGHT NOW.
    # IM WORKING ON IT
    actualcategories = request.form.get("category_ids")
    print(actualcategories)

    name = request.form.get("name")
    link = request.form.get("link")
    category = request.form.get("category")
    difficulty = request.form.get("difficulty")
    problemid = request.form.get("pid")
    print(name, link, category, problemid)

    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE problems SET problem_name=?, problem_link=?, category_id=?, difficulty=? WHERE problem_id = ?", (name, link, category, difficulty, problemid))
    conn.commit()

    cursor.execute("SELECT * FROM problems")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('problems.html', rows=rows)

@app.route('/submitadd' , methods=["POST"])
def submitadd():
    # EXTENSIVE VALIDATION GOES HERE
    # 
    # 

    name = request.form.get("name")
    link = request.form.get("link")
    difficulty = request.form.get("difficulty")
    category = request.form.get("category")

    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO problems (problem_name, problem_link, difficulty, category_id) VALUES (?,?,?,?)" , (name, link, difficulty, category))
    conn.commit()

    cursor.execute("SELECT * FROM problems")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('problems.html', rows=rows)

@app.route('/addproblem', methods=["POST"])
def addproblem():
    return render_template('addproblem.html')

if __name__ == '__main__':
    app.run(debug=True)