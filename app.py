"""
MovieWebApp - Flask Application Setup
-------------------------------------
Initializes Flask, SQLAlchemy, and DataManager.
Supports flexible imports for direct or package-based execution.
Fetches movie details from the OMDb API when adding a movie.
"""

from pathlib import Path
import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

# ---------------------------------------
# FLEXIBLE IMPORTS (works for both `python app.py` and `flask run`)
# ---------------------------------------
try:
    from MovieWebApp.data_manager import DataManager
    from MovieWebApp.models import db, User, Movie
except ModuleNotFoundError:
    from data_manager import DataManager
    from models import db, User, Movie


# ---------------------------------------
# ENVIRONMENT VARIABLES
# ---------------------------------------
load_dotenv()  # Load OMDb API key from .env file
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

if not OMDB_API_KEY:
    print("⚠️  Warning: OMDB_API_KEY not found. Please add it to your .env file.")


# ---------------------------------------
# FLASK APP & DATABASE CONFIGURATION
# ---------------------------------------
app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "movies.db"

# Ensure the data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
db.init_app(app)

# Initialize DataManager
data_manager = DataManager()


# ---------------------------------------
# ROUTES
# ---------------------------------------

@app.route("/")
def home():
    """Home page: lists all users."""
    users = data_manager.get_users()
    return render_template("index.html", users=users)


@app.route("/users", methods=["POST"])
def add_user():
    """Add a new user."""
    name = request.form.get("name")
    if name:
        data_manager.create_user(name)
    return redirect(url_for("home"))


@app.route("/users/<int:user_id>/movies", methods=["GET"])
def user_movies(user_id):
    """Show movies for a specific user."""
    user = User.query.get_or_404(user_id)
    movies = data_manager.get_movies(user_id)
    users = data_manager.get_users()  # for sidebar
    return render_template("movies.html", user=user, movies=movies, users=users)


@app.route("/users/<int:user_id>/movies", methods=["POST"])
def add_movie(user_id):
    movie_name = request.form.get("movie_name")
    if movie_name:
        data_manager.add_movie_from_omdb(movie_name, user_id)
    return redirect(url_for("user_movies", user_id=user_id))


@app.route("/users/<int:user_id>/movies/<int:movie_id>/update", methods=["POST"])
def update_movie(user_id, movie_id):
    """Update a movie title."""
    new_title = request.form.get("new_title")
    if new_title:
        data_manager.update_movie(movie_id, new_title)
    return redirect(url_for("user_movies", user_id=user_id))


@app.route("/users/<int:user_id>/movies/<int:movie_id>/delete", methods=["POST"])
def delete_movie(user_id, movie_id):
    """Delete a movie from user's list."""
    data_manager.delete_movie(movie_id)
    return redirect(url_for("user_movies", user_id=user_id))


@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}


# ---------------------------------------
# ENTRY POINT
# ---------------------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print(f"✅ Database initialized at: {DB_PATH}")

    app.run(host="0.0.0.0", port=5001, debug=True)
