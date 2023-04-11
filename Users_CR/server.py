from flask import Flask, render_template, request, redirect

from users import Users

app = Flask(__name__)

@app.route("/") #First page
def initial():
    return redirect("/users")

@app.route("/users") #to look at all the users in db
def all_users():
    return render_template("read_all.html", users=Users.get_all() )


@app.route("/users/new")
def create():
    return render_template("create.html")

# Must redirect, we never render on a POST
@app.route("/users/add", methods = ["POST"]) #user has filled out form and is submitting it
def process():
    Users.save(request.form)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug = True)