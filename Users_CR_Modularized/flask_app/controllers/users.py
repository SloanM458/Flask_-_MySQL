from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user

@app.route("/")
def welcome():
    pass


@app.route("/users")
def all_users():
    if "first_name" not in session:
        print("Not logged in- going back to root route")
        return redirect("/")
    else:
        print("Now in users")
        print(request.form)#form data now gone from logging in!
        return render_template("read_all.html")
    



@app.route("/users/new", methods = ["POST"])
def new_user():
    pass