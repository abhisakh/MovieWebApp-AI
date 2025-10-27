"""
MovieWebApp - Flask Application Setup
-------------------------------------
Initializes Flask, SQLAlchemy, and DataManager.
Supports flexible imports for direct or package-based execution.
Fetches movie details from the OMDb API when adding a movie.
"""


import re
import os
import secrets
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime


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
# FLASK APP & DATABASE CONFIGURATION
# -----------------------------
app = Flask(__name__)
# Generate a random secret key if none is provided
app.secret_key = os.getenv("FLASK_SECRET_KEY") or secrets.token_hex(16)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "movies.db"

DATA_DIR.mkdir(parents=True, exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

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
    users = data_manager.get_users()
    return render_template("index.html", users=users)


@app.route("/users", methods=["POST"])
def add_user():
    """Add a new user with validation."""
    name = request.form.get("name", "").strip()

    # ✅ Check: non-empty
    if not name:
        flash("⚠️ Name cannot be empty.", "warning")
        return redirect(url_for("home"))

    # ✅ Check: letters and spaces only
    if not re.match(r"^[A-Za-z\s]+$", name):
        flash("⚠️ Name must only contain letters and spaces.", "warning")
        return redirect(url_for("home"))

    # ✅ Check: no duplicates (case-insensitive)
    existing_user = User.query.filter(User.name.ilike(name)).first()
    if existing_user:
        flash(f"⚠️ User '{name}' already exists.", "info")
        return redirect(url_for("home"))

    data_manager.create_user(name)
    flash(f"✅ User '{name}' added successfully!", "success")
    return redirect(url_for("home"))


@app.route("/users/<int:user_id>/movies", methods=["GET"])
def user_movies(user_id):
    """Show movies for a specific user."""
    user = User.query.get_or_404(user_id)
    movies = data_manager.get_movies(user_id)
    users = data_manager.get_users()  # For sidebar or dropdown
    return render_template("movies.html", user=user, movies=movies, users=users)


@app.route("/users/<int:user_id>/movies", methods=["POST"])
def add_movie(user_id):
    """Add a movie either manually or via OMDb lookup."""
    movie_name = request.form.get("movie_name", "").strip()
    director = request.form.get("director", "").strip()
    year = request.form.get("year", "").strip()
    rating = request.form.get("rating", "").strip()

    # ✅ Step 1: Validate required field
    if not movie_name:
        flash("⚠️ Please enter a movie name.", "warning")
        return redirect(url_for("user_movies", user_id=user_id))

    # ✅ Step 2: Prevent duplicates
    existing = Movie.query.filter(
        Movie.user_id == user_id,
        Movie.name.ilike(movie_name)
    ).first()
    if existing:
        flash(f"⚠️ Movie '{movie_name}' already exists in your database.", "info")
        return redirect(url_for("user_movies", user_id=user_id))

    # ✅ Step 3: If user filled director/year/rating — treat as manual entry
    if director or year or rating:
        # Manual input validation
        year_val = None
        if year:
            if not year.isdigit():
                flash("⚠️ Year must be a number.", "warning")
                return redirect(url_for("user_movies", user_id=user_id))
            year_val = int(year)
            if year_val < 1888 or year_val > datetime.now().year + 1:
                flash("⚠️ Please enter a realistic year.", "warning")
                return redirect(url_for("user_movies", user_id=user_id))

        rating_val = None
        if rating:
            try:
                rating_val = float(rating)
                if not (0 <= rating_val <= 10):
                    flash("⚠️ Rating must be between 0 and 10.", "warning")
                    return redirect(url_for("user_movies", user_id=user_id))
            except ValueError:
                flash("⚠️ Rating must be a valid number.", "warning")
                return redirect(url_for("user_movies", user_id=user_id))

        # Save manually
        movie = Movie(
            name=movie_name,
            director=director or "Unknown",
            year=year_val,
            rating=rating_val,
            poster_url="",  # user can edit later
            user_id=user_id
        )
        db.session.add(movie)
        db.session.commit()
        flash(f"✅ '{movie.name}' added manually!", "success")
        return redirect(url_for("user_movies", user_id=user_id))

    # ✅ Step 4: Otherwise → fetch from OMDb
    movie, suggestions = data_manager.add_movie_from_omdb(movie_name, user_id)

    if movie:
        flash(f"✅ '{movie.name}' added from OMDb!", "success")
    else:
        msg = f"❌ Movie '{movie_name}' not found."
        if suggestions:
            formatted = [s.title() for s in suggestions]
            msg += " Did you mean: " + ", ".join(formatted) + "?"
        flash(msg, "error")

    return redirect(url_for("user_movies", user_id=user_id))


@app.route("/users/<int:user_id>/movies/<int:movie_id>/update", methods=["POST"])
def update_movie(user_id, movie_id):
    """Update movie details dynamically with full validation."""
    new_title = request.form.get("new_title", "").strip()
    new_director = request.form.get("new_director", "").strip()
    new_year = request.form.get("new_year", "").strip()
    new_poster = request.form.get("new_poster", "").strip()
    new_rating = request.form.get("new_rating", "").strip()

    # ✅ Validate numeric fields
    year_val = None
    if new_year:
        if not new_year.isdigit():
            flash("⚠️ Year must be a number.", "warning")
            return redirect(url_for("user_movies", user_id=user_id))
        year_val = int(new_year)
        if year_val < 1888 or year_val > datetime.now().year + 1:
            flash("⚠️ Please enter a realistic year.", "warning")
            return redirect(url_for("user_movies", user_id=user_id))

    rating_val = None
    if new_rating:
        try:
            rating_val = float(new_rating)
            if not (0 <= rating_val <= 10):
                flash("⚠️ Rating must be between 0 and 10.", "warning")
                return redirect(url_for("user_movies", user_id=user_id))
        except ValueError:
            flash("⚠️ Rating must be a valid number.", "warning")
            return redirect(url_for("user_movies", user_id=user_id))

    # ✅ Validate URL (optional)
    if new_poster and not re.match(r"^https?://", new_poster):
        flash("⚠️ Poster URL must start with http:// or https://", "warning")
        return redirect(url_for("user_movies", user_id=user_id))

    # Prepare cleaned data
    data = {
        "name": new_title if new_title else None,
        "director": new_director if new_director else None,
        "year": year_val,
        "poster_url": new_poster if new_poster else None,
        "rating": rating_val,
    }

    # Remove None values
    data = {k: v for k, v in data.items() if v is not None}

    # Update in DB
    updated = data_manager.update_movie(movie_id, **data)

    if updated:
        flash(f"✅ Movie '{updated.name}' updated successfully!", "success")
    else:
        flash("❌ Failed to update movie — not found.", "error")

    return redirect(url_for("user_movies", user_id=user_id))


@app.route("/users/<int:user_id>/movies/<int:movie_id>/delete", methods=["POST"])
def delete_movie(user_id, movie_id):
    """Delete a movie from user's list."""
    data_manager.delete_movie(movie_id)
    return redirect(url_for("user_movies", user_id=user_id))


@app.context_processor
def inject_current_year():
    """Inject current year into all templates."""
    return {"current_year": datetime.now().year}

# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print(f"✅ Database initialized at: {DB_PATH}")

    app.run(host="0.0.0.0", port=5001, debug=True)
