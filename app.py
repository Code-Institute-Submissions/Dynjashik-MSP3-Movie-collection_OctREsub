import os
import re
from datetime import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
ADMIN_USER_NAME = 'admin'


mongo = PyMongo(app)


# check if user is admin and set parameter in session before each request
@app.before_request
def before_request():
    if "user" in session:
        session["is_admin"] = session["user"] == ADMIN_USER_NAME
        session["user_logged_in"] = True
    else:
        session["is_admin"] = False
        session["user_logged_in"] = False


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
    return render_template(
        "movies.html", movies=movies, categories=categories, search_str=query)


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    # check if user already logged in, then redirect to home page
    if session["user_logged_in"]:
        return redirect(url_for("home_page"))

    if request.method == "POST":
        username_input = request.form.get("username").lower()
        email_input = request.form.get("email").lower()
        password_input = request.form.get("password")

        # check if username already exists in db
        existing_user = mongo.db.users.find_one({"username": username_input})
        if existing_user:
            flash(["Username " + existing_user["username"]+" already exists"])
            return redirect(url_for("sign_up"))
        has_error = False
        error_msg = []

        # validate username
        if len(username_input) < 4:
            has_error = True
            error_msg.append("Username must be at least 3 characters long")

        # validate email
        is_email_valid, email_error_msg = valid_email_error_msg(email_input)
        if not is_email_valid:
            has_error = True
            error_msg.append(email_error_msg)

        # validate password
        password_regexp = "^[a-zA-Z0-9]{5,16}$"
        valid_password = re.search(password_regexp, password_input)
        if not valid_password:
            has_error = True
            error_msg.append("""Password must be between 5 and 16 characters
                                and consist of letters and numbers""")

        # save new usere to db or throw error(s)
        if has_error:
            flash(error_msg)
            return redirect(url_for("sign_up"))
        else:
            register = {
                "username": username_input,
                "email": email_input,
                "password": generate_password_hash(password_input)
            }
            mongo.db.users.insert_one(register)

            session['registered_user'] = username_input
            flash(["Sign up successful!"])
            return redirect(url_for("sign_in"))

    return render_template("signup.html")


@app.route("/signin", methods=["GET", "POST"])
def sign_in():
    # check if user already logged in, then redirect to home page
    if session["user_logged_in"]:
        return redirect(url_for("home_page"))

    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # validate password
            password_regexp = "^[a-zA-Z0-9]{5,16}$"
            valid_password = re.search(
                password_regexp, request.form.get("password"))
            if not valid_password:
                flash(
                    ["""Password must be between 5 and 16 characters and
                        consist of letters and numbers"""])
                return redirect(url_for("sign_in"))

            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash(["Welcome, {}!".format(request.form.get("username"))])
                return redirect(url_for("home_page"))
            else:
                # invalid password match
                flash(["Invalid password"])
                return redirect(url_for("sign_in"))
        else:
            # username not found
            flash(["Username not found"])
            return redirect(url_for("sign_in"))

    return render_template("signin.html")


@app.route("/profile")
def get_user_profile():
    if not session["user_logged_in"]:
        return redirect(url_for("sign_in"))
    else:
        user_data = mongo.db.users.find_one({'username': session["user"]})
        user_movies = list(
            mongo.db.movies.find({'created_by': session["user"]}))
        return render_template(
            "profile.html", user_data=user_data, user_movies=user_movies)


@app.route("/profile/update", methods=["POST"])
def update_profile():
    if not session["user_logged_in"]:
        abort(404)

    username_input = ""
    if session["is_admin"]:
        username_input = ADMIN_USER_NAME
    elif request.form.get("username"):
        username_input = request.form.get("username").lower()
    email_input = request.form.get("email").lower()
    has_error = False
    error_msg = []

    # validate username
    is_user_valid, user_error_msg = valid_user_return_error_msg(username_input)
    if not is_user_valid:
        has_error = True
        error_msg.append(user_error_msg)

    # validate if username havent changed to admin username
    if not session["is_admin"] and username_input == ADMIN_USER_NAME:
        has_error = True
        error_msg.append("Please pick another username")

    # validate email
    is_email_valid, email_error_msg = valid_email_error_msg(email_input)
    if not is_email_valid:
        has_error = True
        error_msg.append(email_error_msg)

    if has_error:
        flash(error_msg)
        return redirect(url_for("get_user_profile"))
    else:
        mongo.db.users.update({"username": session["user"]},
                              {"$set": {"email": email_input}})
        mongo.db.users.update({"username": session["user"]},
                              {"$set": {"username": username_input}})
        mongo.db.movies.update({"created_by": session["user"]},
                               {"$set": {"created_by": username_input}},
                               multi=True)
        session["user"] = username_input
        flash(["Username information is successfully updated"])
    return redirect(url_for("get_user_profile"))


@app.route("/logout")
def log_out():
    # remove user from session cookie
    flash(["You have been logged out"])
    session.pop("user")
    session["is_admin"] = False
    return redirect(url_for("sign_in"))


@app.route("/movie/add", methods=["GET", "POST"])
def add_movie():
    categories = mongo.db.categories.find().sort("category_name", 1)

    if request.method == "POST":
        movie = {
                "movie_name": request.form.get("movie_name"),
                "category_name": request.form.get("category_name"),
                "year": request.form.get("year"),
                "movie_duration": request.form.get("movie_duration"),
                "movie_description": request.form.get("movie_description"),
                "movie_link": request.form.get("movie_link"),
                "book_link": request.form.get("book_link"),
                "movie_image": request.form.get("movie_image")
        }
        movie_is_valid, error_msg = validate_movie(movie)

        if movie_is_valid:
            movie["created_by"] = session["user"]
            movie["time_added"] = datetime.now()
            mongo.db.movies.insert_one(movie)
            flash(
                ["Movie " + movie["movie_name"] + " is successfully added!"])
            return redirect(url_for("movie_page"))
        else:
            flash(error_msg)
            return redirect(url_for("add_movie", categories=categories))

    return render_template("add_movie.html", categories=categories)


@app.route("/movie/<movie_id>/edit", methods=["GET", "POST"])
def edit_movie(movie_id):
    try:
        movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
        if request.method == "POST":
            submit_movie = {
                "movie_name": request.form.get("movie_name"),
                "movie_link": request.form.get("movie_link"),
                "category_name": request.form.get("category_name"),
                "year": request.form.get("year"),
                "movie_duration": request.form.get("movie_duration"),
                "movie_description": request.form.get("movie_description"),
                "book_link": request.form.get("book_link"),
                "movie_image": request.form.get("movie_image"),
            }
            movie_is_valid, error_msg = validate_movie(submit_movie)
            if movie_is_valid:
                submit_movie["created_by"] = movie["created_by"]
                submit_movie["time_added"] = movie["time_added"]
                mongo.db.movies.update(
                    {"_id": ObjectId(movie_id)}, submit_movie)
                flash(
                    ["Movie "+movie["movie_name"]+" is successfully updated"])
                return redirect(
                    url_for("single_movie_page", movie_id=movie_id))
            else:
                flash(error_msg)
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template(
            "edit_movie.html", movie=movie, categories=categories)
    except:
        return redirect(url_for("home_page"))


@app.route("/movie/<movie_id>", methods=['GET'])
def single_movie_page(movie_id):
    try:
        movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
        return render_template("movie.html", movie=movie)
    except:
        return redirect(url_for("home_page"))


@app.route("/movie/<movie_id>/delete")
def delete_movie(movie_id):
    try:
        mongo.db.movies.remove({"_id": ObjectId(movie_id)})
        flash(["Movie is successfully deleted"])
        return redirect(url_for("movie_page"))
    except:
        return redirect(url_for("home_page"))


@app.route("/categories")
def get_categories():
    if not session["user_logged_in"] or not session["is_admin"]:
        abort(404)
    else:
        categories = list(mongo.db.categories.find().sort("category_name", 1))
        return render_template("categories.html", categories=categories)


@app.route("/category/add", methods=["GET", "POST"])
def add_category():
    if not session["user_logged_in"] or not session["is_admin"]:
        abort(404)
    else:
        if request.method == "POST":
            categories = mongo.db.categories.find()
            new_category = request.form.get("category_name").capitalize()
            for category in categories:
                if category["category_name"] == new_category:
                    flash(["The category already exists"])
                    return redirect(url_for("add_category"))
            category_dict = {
                "category_name": request.form.get("category_name").capitalize()
            }
            mongo.db.categories.insert_one(category_dict)
            flash(["New category is successfully added"])
            return redirect(url_for("get_categories"))

        return render_template("add_category.html")


@app.route("/category/<category_id>/delete")
def delete_category(category_id):
    if not session["user_logged_in"] or not session["is_admin"]:
        abort(404)

    try:
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash(["Category is successfully deleted"])
    except:
        return redirect(url_for("get_categories"))

    return redirect(url_for("get_categories"))


def validate_movie(movie):
    is_valid = True
    error_msg = []
    # validate movie name
    if len(movie["movie_name"]) < 1:
        is_valid = False
        error_msg.append("Movie name should be at least 1 character long")

    # validate category
    if not movie["category_name"]:
        is_valid = False
        error_msg.append("Category is not selected")

    # validate year
    if not (movie["year"].isnumeric() and 1899 < int(movie["year"]) < 2101):
        is_valid = False
        error_msg.append("Year must be a number between 1990 and 2100")

    # validate duration
    if not (movie["movie_duration"].isnumeric() and
            int(movie["movie_duration"]) > 0):
        is_valid = False
        error_msg.append("Duration must be a positive number")

    # validate description
    if len(movie["movie_description"]) < 11:
        is_valid = False
        error_msg.append("Description must be at least 10 characters")

    # validate book link
    if not movie["book_link"]:
        is_valid = False
        error_msg.append("Book link must be specified")

    # validate movie link
    if not movie["movie_link"]:
        is_valid = False
        error_msg.append("Movie link must be specified")

    return is_valid, error_msg


def valid_user_return_error_msg(username):
    if len(username) < 3:
        return False, "Username must be at least 3 characters long \n"
    return True, ""


def valid_email_error_msg(email):
    email_regexp = "[a-z0-9._%+-]+@[a-z0-9.-]+.[a-zA-Z]{2,4}$"
    valid_email = re.search(email_regexp, email)
    if not valid_email:
        return False, "Not valid email \n"
    return True, ""


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
