import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/movies")
def movie_page():
    movies = list(mongo.db.movies.find())
    print("wow")
    return render_template("movies.html", movies=movies)


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_in"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # add the new user into collection users
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")

    return render_template("signup.html")


@app.route("/signin", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        print (existing_user)
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("home_page"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("sign_in"))

    return render_template("signin.html")


@app.route("/logout")
def log_out():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        movie = {
            "movie_name": request.form.get("movie_name"),
            "category_name": request.form.get("category_name"),
            "year": request.form.get("year"),
            "movie_duration": request.form.get("movie_duration"),
            "movie_description": request.form.get("movie_description"),
            "book_link": request.form.get("book_link"),
            "created_by": session["user"]
        }
        mongo.db.movies.insert_one(movie)
        flash("Movie is Successfully Added")
        return redirect(url_for("movie_page"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_movie.html", categories=categories)


@app.route("/edit_movie/<movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_movie.html", movie=movie, categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)