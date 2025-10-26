# data_manager.py
import os
import requests
from dotenv import load_dotenv

try:
    from MovieWebApp.models import db, User, Movie
except ModuleNotFoundError:
    from models import db, User, Movie

# Load environment variables
load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")


class DataManager:
    """Class to manage CRUD operations for Users and Movies, including OMDb fetching."""

    # -------------------------
    # USER OPERATIONS
    # -------------------------
    def create_user(self, name: str) -> User:
        """Add a new user to the database."""
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return user

    def get_users(self) -> list[User]:
        """Return a list of all users."""
        return User.query.all()

    # -------------------------
    # MOVIE OPERATIONS
    # -------------------------
    def get_movies(self, user_id: int) -> list[Movie]:
        """Return all movies belonging to a specific user."""
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, movie: Movie) -> Movie:
        """Add a new movie to a user's favorites after creating movie object first."""
        db.session.add(movie)
        db.session.commit()
        return movie

    def add_movie_from_omdb(self, movie_name: str, user_id: int) -> Movie | None:
        """Fetch movie details from OMDb API and add to the database."""
        if not OMDB_API_KEY:
            print("⚠️ Missing OMDb API key.")
            return None

        params = {"t": movie_name, "apikey": OMDB_API_KEY}
        response = requests.get("https://www.omdbapi.com/", params=params)

        if response.status_code != 200:
            print("❌ OMDb request failed.")
            return None

        data = response.json()
        if data.get("Response") == "False":
            print(f"⚠️ Movie '{movie_name}' not found on OMDb.")
            return None

        rating_str = data.get("imdbRating", "0.0")
        rating = float(rating_str) if rating_str.replace(".", "").isdigit() else 0.0

        movie = Movie(
            name=data.get("Title", movie_name),
            director=data.get("Director", "Unknown"),
            year=int(data.get("Year", 0)) if data.get("Year", "0").isdigit() else 0,
            poster_url=data.get("Poster", ""),
            user_id=user_id,
            rating=rating
        )
        db.session.add(movie)
        db.session.commit()
        return movie

    def update_movie(self, movie_id: int, new_title: str) -> Movie:
        """Update the title of a specific movie."""
        movie = Movie.query.get(movie_id)
        if movie:
            movie.name = new_title
            db.session.commit()
        return movie

    def delete_movie(self, movie_id: int) -> bool:
        """Delete a movie from the database."""
        movie = Movie.query.get(movie_id)
        if movie:
            db.session.delete(movie)
            db.session.commit()
            return True
        return False
