from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/major/')
def major():
    return render_template("index.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/problems/')
def problems():
    return render_template("problems.html")

@app.route('/resources/')
def resources():
    return render_template("resources.html")

####### DISABLED TIL WE DECIDE HOW TO HANDLE LOGIN #######

# @app.route('/user/<name>/')
# def user(name):
#     return f"Hello {name}!"

# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     return render_template("login.html")

# @app.route('/admin/')
# def admin():
#     return redirect(url_for("user", name='Admin!'))

if __name__ == "__main__":
    app.run(debug=True, port=5001)