import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
ADMIN_USER_NAME = 'admin'


mongo = PyMongo(app)


@app.before_request
def before_request():
    if "user" in session:
        session["is_admin"] = session["user"] == ADMIN_USER_NAME
    else:
        session["is_admin"] = False


@app.route("/")
@app.route("/home")
def home_page():
    recently_added_movies = list(
        mongo.db.movies.find().sort("time_added", -1).limit(3))
    return render_template(
        "home.html", recently_added_movies=recently_added_movies)


@app.route("/movies")
def movie_page():
    movies = list(mongo.db.movies.find())
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("movies.html", movies=movies, categories=categories)


@app.route("/movies/<category>")
def movie_page_filtered(category):
    movies = list(mongo.db.movies.find({'category_name': category}))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("movies.html", movies=movies, categories=categories)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    movies = list(mongo.db.movies.find({"$text": {"$search": query}}))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("movies.html", movies=movies, categories=categories, search_str=query)


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    # check if user already logged in, then redirect to home page
    if "user" in session:
        return redirect(url_for("home_page"))

    if request.method == "POST":
        username_input = request.form.get("username").lower()
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": username_input})

        if existing_user:
            flash("Username " + existing_user["username"] + " already exists")
            return redirect(url_for("sign_up"))

        register = {
            "username": username_input,
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session['registered_user'] = username_input
        flash("Sign up successful!")
        return redirect(url_for("sign_in"))

    return render_template("signup.html")


@app.route("/signin", methods=["GET", "POST"])
def sign_in():
    # check if user already logged in, then redirect to home page
    if "user" in session:
        return redirect(url_for("home_page"))
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}!".format(request.form.get("username")))
                    return redirect(url_for("home_page"))
            else:
                # invalid password match
                flash("Invalid password")
                return redirect(url_for("sign_in"))

        else:
            # username doesn't exist
            flash("Username doesn't exist")
            return redirect(url_for("sign_in"))

    return render_template("signin.html")


@app.route("/logout")
def log_out():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/movie/add", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        movie = {
            "movie_name": request.form.get("movie_name"),
            "movie_link": request.form.get("movie_link"),
            "category_name": request.form.get("category_name"),
            "year": request.form.get("year"),
            "movie_duration": request.form.get("movie_duration"),
            "movie_description": request.form.get("movie_description"),
            "book_link": request.form.get("book_link"),
            "movie_image": request.form.get("movie_image"),
            "created_by": session["user"],
            "time_added": datetime.now()
        }
        mongo.db.movies.insert_one(movie)
        flash("Movie is successfully added!")
        return redirect(url_for("movie_page"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_movie.html", categories=categories)


@app.route("/movie/<movie_id>/edit", methods=["GET", "POST"])
def edit_movie(movie_id):
    if request.method == "POST":
        submit = {
            "movie_name": request.form.get("movie_name"),
            "movie_link": request.form.get("movie_link"),
            "category_name": request.form.get("category_name"),
            "year": request.form.get("year"),
            "movie_duration": request.form.get("movie_duration"),
            "movie_description": request.form.get("movie_description"),
            "book_link": request.form.get("book_link"),
            "movie_image": request.form.get("movie_image"),
        }
        mongo.db.movies.update({"_id": ObjectId(movie_id)}, submit)
        flash("Movie is successfully updated")

    movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_movie.html", movie=movie, categories=categories)


@app.route("/movie/<movie_id>/delete")
def delete_movie(movie_id):
    mongo.db.movies.remove({"_id": ObjectId(movie_id)})
    flash("Movie is successfully deleted")
    return redirect(request.referrer)


@app.route("/categories")
def get_categories():
    if not session["user"] or not session["is_admin"]:
        abort(404)
    else:
        categories = list(mongo.db.categories.find().sort("category_name", 1))
        return render_template("categories.html", categories=categories)


@app.route("/category/add", methods=["GET", "POST"])
def add_category():
    if not session["user"] or session["user"] != ADMIN_USER_NAME:
        abort(404)
    else:
        if request.method == "POST":
            categories = mongo.db.categories.find()
            new_category = request.form.get("category_name").capitalize()
            for category in categories:
                if category["category_name"] == new_category:
                    flash("The category already exists")
                    return redirect(url_for("add_category"))
            category_dict = {
                "category_name": request.form.get("category_name").capitalize()
            }
            mongo.db.categories.insert_one(category_dict)
            flash("New category is successfully added")
            return redirect(url_for("get_categories"))

        return render_template("add_category.html")


@app.route("/category/<category_id>/delete")
def delete_category(category_id):
    if not session["user"] or session["user"] != ADMIN_USER_NAME:
        abort(404)
    else:
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("Category is successfully deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
