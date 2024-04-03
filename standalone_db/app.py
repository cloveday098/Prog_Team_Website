from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

global newdict
newdict = {}
conn = sqlite3.connect('logins.db')
cursor = conn.cursor()
cursor.execute("SELECT * from categories")
res = cursor.fetchall()

for grp in res:
    newdict[grp[0]] = grp[1]

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
    print("rows:" , rows)
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    cursor.execute("SELECT * FROM problemscategories")
    pr = cursor.fetchall()
    return render_template('problems.html', rows=rows, categories=categories, cats=pr, fr = newdict)

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

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('problems.html' , rows=rows, categories=categories, fr = newdict)

@app.route('/editproblem', methods=["POST" , "GET"])
def editproblem():
    problemid = request.args.get("problemid")
    print("PROBLEMID:" , problemid)
    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM problems where problem_id=?", ((problemid,)))
    rows = cursor.fetchall()

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    print("ROWSSSS:" , rows)

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

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    cursor.execute("SELECT * FROM problemscategories")
    pr = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('problems.html' , rows=rows, categories=categories, cats = pr, fr = newdict)

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

    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()

    catsAndIdsDict = {}

    actualcategories = request.form.getlist("categories")
    print("actualcategories" , actualcategories)

    tst = request.form.getlist("category_ids")
    print("tst" , tst)

    cats = []

    name = request.form.get("name")
    link = request.form.get("link")
    category = request.form.get("category")
    difficulty = request.form.get("difficulty")
    problemid = request.form.get("pid")
    print(name, link, category, problemid)

    cursor.execute("DELETE FROM problemscategories WHERE problem_id=?" , (problemid,))
    conn.commit()

    counter = 0

    for cat in actualcategories:
        # here, we iterate through the list and append rows to a hybrid table
        cursor.execute("SELECT category_name FROM categories WHERE category_id=?",(int(cat),))
        cname = cursor.fetchone()
        print(cname[0])

        cursor.execute("INSERT INTO problemscategories (problem_id , category_id) VALUES (? , ?)" , (problemid , int(cat)))
        conn.commit()

        cursor.execute("SELECT * FROM problemscategories WHERE problem_id = ?" , (problemid,))
        testing = cursor.fetchall()
        print(testing)

        cursor.execute("SELECT * FROM problemscategories")
        pr = cursor.fetchall()
        print("Whole table:")
        print(pr)

        cursor.execute("SELECT category_name FROM CATEGORIES WHERE category_id = ?" , (testing[counter][1] , ))
        cactual = cursor.fetchone()

        cats.append(cactual)

        counter = counter + 1
    
    print("CATS" , cats)

    for cat in cats:
        print(cat[0])
        cursor.execute("SELECT category_id FROM CATEGORIES WHERE category_name = ?" , (cat[0],))
        tempId = cursor.fetchone()
        catsAndIdsDict[tempId[0]] = cat[0]
    
    print("dictionary:" , catsAndIdsDict)

    conn.commit()

    cursor.execute("UPDATE problems SET problem_name=?, problem_link=?, category_id=?, difficulty=? WHERE problem_id = ?", (name, link, category, difficulty, problemid))
    conn.commit()

    cursor.execute("SELECT * FROM problems")

    rows = cursor.fetchall()
    print("rows:" , rows)
    print("col[0]" , pr[0])

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('problems.html', rows=rows, cats=pr, dct = catsAndIdsDict, fr = newdict)

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
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('problems.html', rows=rows, categories=categories , fr = newdict)

@app.route('/addproblem', methods=["POST"])
def addproblem():
    return render_template('addproblem.html')

if __name__ == '__main__':
    app.run(debug=True)