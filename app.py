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
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("movies.html", movies=movies, categories=categories)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    movies = list(mongo.db.movies.find({"$text": {"$search": query}}))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("movies.html", movies=movies, categories=categories)


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username_input = request.form.get("username")
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": username_input.lower()})

        if existing_user:
            flash("Username " + existing_user["username"] + " already exists")
            return redirect(url_for("sign_up"))

        register = {
            "username": username_input.lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session['registered_user'] = username_input
        flash("Sign Up Successful!")
        return redirect(url_for("sign_in"))

    return render_template("signup.html")


@app.route("/signin", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}!".format(request.form.get("username")))
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
            "movie_image": request.form.get("movie_image"),
            "created_by": session["user"]
        }
        mongo.db.movies.insert_one(movie)
        flash("Movie is successfully added!")
        return redirect(url_for("movie_page"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_movie.html", categories=categories)


@app.route("/edit_movie/<movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    if request.method == "POST":
        submit = {
            "movie_name": request.form.get("movie_name"),
            "category_name": request.form.get("category_name"),
            "year": request.form.get("year"),
            "movie_duration": request.form.get("movie_duration"),
            "movie_description": request.form.get("movie_description"),
            "book_link": request.form.get("book_link"),
            "movie_image": request.form.get("movie_image"),
            "created_by": session["user"]
        }
        mongo.db.movies.update({"_id": ObjectId(movie_id)}, submit)
        flash("Movie is Successfully Updated")

    movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_movie.html", movie=movie, categories=categories)


@app.route("/delete_movie/<movie_id>")
def delete_movie(movie_id):
    mongo.db.movies.remove({"_id": ObjectId(movie_id)})
    flash("Movie Successfully Deleted")
    return redirect(url_for("movie_page"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
