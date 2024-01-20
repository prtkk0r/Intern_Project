from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("records")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS usr_data (name varchar(100), email varchar(50), username varchar(50) PRIMARY KEY, password varchar(15));")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/auth.html",methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        username = request.form["usr"]
        password = request.form["pwd"]
        print(username,password)
        
        conn = sqlite3.connect("records")
        cur = conn.cursor()
        cur.execute(f'''SELECT password FROM usr_data WHERE username = "{username}";''')
        pwd = cur.fetchone()[0]
        
        if pwd == password:
            return render_template("accessed.html")
        else:
            return render_template("auth.html")
        
    else:
        return  render_template("auth.html")

@app.route("/register.html",methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        username = request.form["usr"]
        password = request.form["pwd"]
        c_password = request.form["c_pwd"]
        print(name,email,username,password,c_password)

        if c_password == password:
            conn = sqlite3.connect("records")
            cur = conn.cursor()
            cur.execute('''INSERT INTO usr_data (name,email,username,password) values(?,?,?,?);''',(name,email,username,password))
            cur.execute("commit;")
            return render_template("auth.html")
        else:
            return render_template("register.html")
        
    else:
        return render_template("register.html")

@app.route("/accessed.html")
def access():
    return render_template("accessed.html")

if __name__ == "__main__":
    app.run(debug=True)