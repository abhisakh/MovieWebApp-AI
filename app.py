"""
MovieWebApp - Flask Application Setup
-------------------------------------
Initializes Flask, SQLAlchemy, and DataManager.
Supports flexible imports for direct or package-based execution.
Fetches movie details from the OMDb API when adding a movie.
Includes error handling and logging.
"""

import re
import os
import secrets
import logging
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from flask import (
    Flask, render_template, request, redirect, url_for, flash
)
import requests

# -----------------------------
# FLEXIBLE IMPORTS
# -----------------------------
try:
    from MovieWebApp.data_manager import DataManager
    from MovieWebApp.models import db, User, Movie
except ModuleNotFoundError:
    from data_manager import DataManager
    from models import db, User, Movie

# -----------------------------
# ENVIRONMENT VARIABLES
# -----------------------------
load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

if not OMDB_API_KEY:
    print("⚠️ Warning: OMDB_API_KEY not found. Add it to your .env file.")

# -----------------------------
# LOGGING CONFIGURATION
# -----------------------------
logging.basicConfig(
    filename="app_errors.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
)

# -----------------------------
# FLASK APP & DATABASE CONFIGURATION
# -----------------------------
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY") or secrets.token_hex(16)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "movies.db"

DATA_DIR.mkdir(parents=True, exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# -----------------------------
# GitHub Cnnfiguration for the contact form
# -----------------------------
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_OWNER = "abhisakh"
REPO_NAME = "MovieWebApp"

# -----------------------------
# DATA MANAGER
# -----------------------------
data_manager = DataManager()

# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def home():
    """Home page: lists all users."""
    try:
        users = data_manager.get_users()
        return render_template("index.html", users=users, request=request)
    except Exception as e:
        logging.error(e)
        flash("❌ Failed to load users.", "error")
        return render_template("index.html", users=[], request=request)


@app.route("/users", methods=["POST"])
def add_user():
    """Add a new user with validation."""
    name = request.form.get("name", "").strip()
    try:
        if not name:
            flash("⚠️ Name cannot be empty.", "warning")
            return redirect(url_for("home"))

        if not re.match(r"^[A-Za-z\s]+$", name):
            flash("⚠️ Name must only contain letters and spaces.", "warning")
            return redirect(url_for("home"))

        existing_user = User.query.filter(User.name.ilike(name)).first()
        if existing_user:
            flash(f"⚠️ User '{name}' already exists.", "info")
            return redirect(url_for("home"))

        data_manager.create_user(name)
        flash(f"✅ User '{name}' added successfully!", "success")
        return redirect(url_for("home"))

    except Exception as e:
        logging.error(e)
        flash("❌ Failed to add user.", "error")
        return redirect(url_for("home"))


@app.route("/users/<int:user_id>/movies", methods=["GET"])
def user_movies(user_id):
    """Show movies for a specific user."""
    try:
        user = User.query.get_or_404(user_id)
        movies = data_manager.get_movies(user_id)
        users = data_manager.get_users()  # Add users for consistent nav
        return render_template("movies.html", user=user, movies=movies, users=users, request=request)
    except Exception as e:
        logging.error(e)
        flash("❌ Failed to load user movies.", "error")
        return redirect(url_for("home"))


@app.route("/users/<int:user_id>/movies", methods=["POST"])
def add_movie(user_id):
    """Add a movie manually or via OMDb API."""
    movie_name = request.form.get("movie_name", "").strip()
    director = request.form.get("director", "").strip()
    year = request.form.get("year", "").strip()
    rating = request.form.get("rating", "").strip()

    try:
        if not movie_name:
            flash("⚠️ Please enter a movie name.", "warning")
            return redirect(url_for("user_movies", user_id=user_id))

        existing = Movie.query.filter(
            Movie.user_id == user_id,
            Movie.name.ilike(movie_name)
        ).first()
        if existing:
            flash(f"⚠️ Movie '{movie_name}' already exists.", "info")
            return redirect(url_for("user_movies", user_id=user_id))

        # Manual input
        year_val, rating_val = None, None
        if director or year or rating:
            if year:
                if not year.isdigit():
                    flash("⚠️ Year must be a number.", "warning")
                    return redirect(url_for("user_movies", user_id=user_id))
                year_val = int(year)
                if year_val < 1888 or year_val > datetime.now().year + 1:
                    flash("⚠️ Please enter a realistic year.", "warning")
                    return redirect(url_for("user_movies", user_id=user_id))

            if rating:
                try:
                    rating_val = float(rating)
                    if not (0 <= rating_val <= 10):
                        flash("⚠️ Rating must be between 0 and 10.", "warning")
                        return redirect(url_for("user_movies", user_id=user_id))
                except ValueError:
                    flash("⚠️ Rating must be a valid number.", "warning")
                    return redirect(url_for("user_movies", user_id=user_id))

            movie = Movie(
                name=movie_name,
                director=director or "Unknown",
                year=year_val,
                rating=rating_val,
                poster_url="",
                user_id=user_id
            )
            db.session.add(movie)
            db.session.commit()
            flash(f"✅ '{movie.name}' added manually!", "success")
            return redirect(url_for("user_movies", user_id=user_id))

        # OMDb fetch
        movie, suggestions = data_manager.add_movie_from_omdb(movie_name, user_id)
        if movie:
            flash(f"✅ '{movie.name}' added from OMDb!", "success")
        else:
            msg = f"❌ Movie '{movie_name}' not found."
            if suggestions:
                msg += " Did you mean: " + ", ".join([s.title() for s in suggestions]) + "?"
            flash(msg, "error")

        return redirect(url_for("user_movies", user_id=user_id))

    except Exception as e:
        logging.error(e)
        flash("❌ Failed to add movie.", "error")
        return redirect(url_for("user_movies", user_id=user_id))


@app.route("/users/<int:user_id>/movies/<int:movie_id>/update", methods=["POST"])
def update_movie(user_id, movie_id):
    """Update movie details with validation."""
    new_title = request.form.get("new_title", "").strip()
    new_director = request.form.get("new_director", "").strip()
    new_year = request.form.get("new_year", "").strip()
    new_poster = request.form.get("new_poster", "").strip()
    new_rating = request.form.get("new_rating", "").strip()

    try:
        year_val, rating_val = None, None
        if new_year:
            if not new_year.isdigit():
                flash("⚠️ Year must be a number.", "warning")
                return redirect(url_for("user_movies", user_id=user_id))
            year_val = int(new_year)
            if year_val < 1888 or year_val > datetime.now().year + 1:
                flash("⚠️ Please enter a realistic year.", "warning")
                return redirect(url_for("user_movies", user_id=user_id))

        if new_rating:
            try:
                rating_val = float(new_rating)
                if not (0 <= rating_val <= 10):
                    flash("⚠️ Rating must be between 0 and 10.", "warning")
                    return redirect(url_for("user_movies", user_id=user_id))
            except ValueError:
                flash("⚠️ Rating must be a valid number.", "warning")
                return redirect(url_for("user_movies", user_id=user_id))

        if new_poster and not re.match(r"^https?://", new_poster):
            flash("⚠️ Poster URL must start with http:// or https://", "warning")
            return redirect(url_for("user_movies", user_id=user_id))

        data = {k: v for k, v in {
            "name": new_title or None,
            "director": new_director or None,
            "year": year_val,
            "poster_url": new_poster or None,
            "rating": rating_val
        }.items() if v is not None}

        updated = data_manager.update_movie(movie_id, **data)
        if updated:
            flash(f"✅ Movie '{updated.name}' updated successfully!", "success")
        else:
            flash("❌ Failed to update movie — not found.", "error")

        return redirect(url_for("user_movies", user_id=user_id))

    except Exception as e:
        logging.error(e)
        flash("❌ Failed to update movie.", "error")
        return redirect(url_for("user_movies", user_id=user_id))


@app.route("/users/<int:user_id>/movies/<int:movie_id>/delete", methods=["POST"])
def delete_movie(user_id, movie_id):
    """Delete a movie from user's list."""
    try:
        data_manager.delete_movie(movie_id)
        flash("✅ Movie deleted successfully!", "success")
        return redirect(url_for("user_movies", user_id=user_id))
    except Exception as e:
        logging.error(e)
        flash("❌ Failed to delete movie.", "error")
        return redirect(url_for("user_movies", user_id=user_id))


@app.route("/about")
def about():
    return render_template("about.html")


# -----------------------------
# ERROR HANDLERS
# -----------------------------
@app.errorhandler(404)
def page_not_found(e):
    """404 Page Not Found."""
    logging.error(e)
    users = data_manager.get_users()
    flash("❌ Page not found.", "error")
    return render_template("404.html", request=request, users=users), 404


@app.errorhandler(500)
def internal_server_error(e):
    """500 Internal Server Error."""
    logging.error(e)
    users = data_manager.get_users()
    flash("❌ Something went wrong on the server.", "error")
    return render_template("500.html", request=request, users=users), 500


# -----------------------------
# CONTEXT PROCESSOR
# -----------------------------
@app.context_processor
def inject_globals():
    """Inject common variables into all templates."""
    try:
        users = data_manager.get_users()
    except Exception as e:
        logging.error(f"Failed to load users for context processor: {e}")
        users = []

    return {
        "current_year": datetime.now().year,
        "users": users
    }


# -----------------------------
# GITHUB ROUTE
# -----------------------------
def save_contact_to_github(name, email, message):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    data = {
        "title": f"Contact: {name} ({email})",
        "body": message
    }
    response = requests.post(url, json=data, headers=headers)
    return response.status_code == 201  # True if issue created


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # -----------------------------
        # VALIDATION
        # -----------------------------
        if not name:
            flash("⚠️ Name cannot be empty.", "warning")
            return redirect(url_for("home"))

        if not re.match(r"^[A-Za-z\s]+$", name):
            flash("⚠️ Name must only contain letters and spaces.", "warning")
            return redirect(url_for("home"))

        # Optional: validate email format
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_pattern, email):
            flash("⚠️ Please enter a valid email address.", "warning")
            return redirect(url_for("contact"))

        # -----------------------------
        # SEND TO GITHUB
        # -----------------------------
        if save_contact_to_github(name, email, message):
            flash("✅ Your message has been sent!", "success")
        else:
            flash("❌ Failed to send message. Try again later.", "error")

        return redirect(url_for("contact"))

    return render_template("contact.html")



# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print(f"✅ Database initialized at: {DB_PATH}")
        print("🚀 Flask app running at: http://127.0.0.1:5001")  # 👈 Add this line
    app.run(host="0.0.0.0", port=5001, debug=True)

