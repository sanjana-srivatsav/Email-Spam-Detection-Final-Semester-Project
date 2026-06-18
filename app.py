from flask import Flask, render_template, request, redirect, session
import sqlite3
import pickle

DB_PATH = r"C:\Users\Admin\OneDrive\Desktop\Email Spam Detection Project\users.db"
app = Flask(__name__)
app.secret_key = "spamproject"

# Load trained model
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------- WELCOME PAGE ----------------


@app.route("/")
def welcome():
    return render_template("welcome.html")
# ------------------HOME ----------------------


@app.route("/home")
def index():
    return render_template("index.html")


# ---------- Login page ----------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE username=? AND password=?",
                    (username, password))

        data = cur.fetchone()

        conn.close()

        if data:

            role = data[0]
            session["username"] = username
            session["role"] = role

            if role == "admin":
                return redirect("/admin")
            else:
                return redirect("/predict")
        else:
            return "Invalid Login"

    return render_template("login.html")

# ---------------- REGISTER ---------------


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("INSERT INTO users(username, password, role) VALUES(?, ?, ?)",
                    (username, password, "user"))

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

# -------------------------USER PREDICT PAGE ---------------


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if "username" not in session:
        return redirect("/login")

    if session["role"] == "admin":
        return redirect("/admin")

    result = None

    if request.method == "POST":

        message = request.form["message"]

        data = vectorizer.transform([message])
        prediction = model.predict(data)[0]

        if prediction == 1:
            result = "Spam"
        else:
            result = "Not Spam"

        # Save result to DB
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO history(username, message, result) VALUES(?, ?, ?)",
            (session["username"], message, result)
        )

        conn.commit()
        conn.close()

    return render_template("spam_checker.html", result=result)

# -------------- ADMIN DASHBOARD ----------------


@app.route("/admin")
def admin():

    if "username" not in session:
        return redirect("/login")

    if session["role"] != "admin":
        return redirect("/predict")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT username,role FROM users")
    users = cur.fetchall()

    cur.execute("SELECT COUNT(*) FROM history WHERE result='Spam'")
    spam = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM history WHERE result='Not Spam'")
    ham = cur.fetchone()[0]

    conn.close()

    return render_template("admin.html", users=users, spam=spam, ham=ham)

# --------------LOGOUT ----------------


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
