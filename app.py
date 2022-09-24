import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///courses.db")

# Loads index page
@app.route("/")
def index():
    return render_template("index.html")

# Loads courses page
@app.route("/courses")
def courses():
    courses = db.execute("SELECT * FROM courses")
    return render_template("courses.html", courses=courses)

# Loads registration page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        courses = db.execute("SELECT name FROM courses")
        return render_template("register.html", courses=courses)

    else:
        # Ensures the user fills out all required fields
        if not request.form.get("lname"):
            return render_template("error.html", value="last name")

        elif not request.form.get("sex"):
            return render_template("error.html", value="sex")

        elif not request.form.get("age"):
            return render_template("error.html", value="age")

        elif int(request.form.get("age")) < 13 or int(request.form.get("age")) > 65:
            return render_template("error.html", value="age")

        elif not request.form.get("nationality"):
            return render_template("error.html", value="nationality")

        elif not request.form.get("email"):
            return render_template("error.html", value="email")

        elif not request.form.get("course"):
            return render_template("error.html", value="course")

        else:
            courses = db.execute("SELECT name FROM courses")
            tmp = []
            for course in courses:
                name = course["name"]
                tmp.append(name)
            if request.form.get("course") not in tmp:
                return render_template("error.html", value="course")

            # Extracts required information from form
            else:
                fname = request.form.get("fname")
                lname = request.form.get("lname")
                sex = request.form.get("sex")
                age = request.form.get("age")
                nationality = request.form.get("nationality")
                course = request.form.get("course")
                email = request.form.get("email")

                # Loads profile page with required inputs
                return render_template("profile.html", fname=fname, lname=lname, sex=sex, age=age, nationality=nationality, email=email, course=course)


