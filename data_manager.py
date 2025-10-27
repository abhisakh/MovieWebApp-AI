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
    """Manage CRUD operations for Users and Movies, including OMDb fetching."""

    # -------------------------
    # USER OPERATIONS
    # -------------------------
    def create_user(self, name: str) -> User:
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return user

    def get_users(self) -> list[User]:
        return User.query.all()

    # -------------------------
    # MOVIE OPERATIONS
    # -------------------------
    def get_movies(self, user_id: int) -> list[Movie]:
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, movie: Movie) -> Movie:
        db.session.add(movie)
        db.session.commit()
        return movie

    # -------------------------
    # OMDb OPERATIONS
    # -------------------------
    def add_movie_from_omdb(self, movie_name: str, user_id: int) -> tuple[Movie | None, list[str], bool]:
        movie_name = movie_name.strip()
        if not movie_name or not OMDB_API_KEY:
            return None, [], False

        # Check if movie already exists in DB
        existing = Movie.query.filter(
            Movie.user_id == user_id,
            Movie.name.ilike(movie_name)
        ).first()
        if existing:
            return existing, [], False  # movie exists, not newly added

        # Try exact match first
        try:
            response = requests.get(
                "https://www.omdbapi.com/",
                params={"t": movie_name, "apikey": OMDB_API_KEY},
                timeout=5
            )
            response.raise_for_status()
            data = response.json()
        except requests.RequestException:
            data = {}

        if data.get("Response") == "True" and data.get("Title", "").lower() == movie_name.lower():
            try:
                rating = float(data.get("imdbRating", 0))
            except (ValueError, TypeError):
                rating = 0.0
            try:
                year = int(data.get("Year", 0))
            except (ValueError, TypeError):
                year = 0

            movie = Movie(
                name=data.get("Title"),
                director=data.get("Director", "Unknown"),
                year=year,
                poster_url=data.get("Poster", ""),
                user_id=user_id,
                rating=rating
            )
            db.session.add(movie)
            db.session.commit()
            return movie, [], True  # newly added

        # Exact match failed → nearest suggestions
        padded_query = movie_name if len(movie_name) > 2 else f"{movie_name}  "
        try:
            search_response = requests.get(
                "https://www.omdbapi.com/",
                params={"s": padded_query, "apikey": OMDB_API_KEY},
                timeout=5
            )
            search_response.raise_for_status()
            search_data = search_response.json()
        except requests.RequestException:
            return None, [], False

        if search_data.get("Response") == "True":
            search_results = search_data.get("Search", [])
            nearest_titles = [m.get("Title") for m in search_results[:5]]  # top 5 suggestions
            return None, nearest_titles, False

        return None, [], False


    # -------------------------
    # HELPER METHODS
    # -------------------------
    def _fetch_movie_by_title(self, title: str, user_id: int) -> Movie | None:
        """Fetch full movie details using OMDb title search (t=)."""
        if not OMDB_API_KEY:
            return None
        params = {"t": title, "apikey": OMDB_API_KEY}
        try:
            response = requests.get("https://www.omdbapi.com/", params=params, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            return None

        data = response.json()
        if data.get("Response") == "False":
            return None
        return self._create_movie_from_data(data, user_id)

    def _fetch_movie_by_imdb_id(self, imdb_id: str, user_id: int) -> Movie | None:
        """Fetch full movie details using IMDb ID (i=)."""
        if not OMDB_API_KEY:
            return None
        params = {"i": imdb_id, "apikey": OMDB_API_KEY}
        try:
            response = requests.get("https://www.omdbapi.com/", params=params, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            return None

        data = response.json()
        if data.get("Response") == "False":
            return None
        return self._create_movie_from_data(data, user_id)

    def _create_movie_from_data(self, data: dict, user_id: int) -> Movie | None:
        """Create and store a Movie object from OMDb data."""
        try:
            rating = float(data.get("imdbRating", 0))
        except (ValueError, TypeError):
            rating = 0.0

        try:
            year = int(data.get("Year", 0))
        except (ValueError, TypeError):
            year = 0

        movie = Movie(
            name=data.get("Title", "Unknown"),
            director=data.get("Director", "Unknown"),
            year=year,
            poster_url=data.get("Poster", ""),
            user_id=user_id,
            rating=rating
        )
        db.session.add(movie)
        db.session.commit()
        return movie

    # -------------------------
    # UPDATE & DELETE
    # -------------------------
    def update_movie(self, movie_id: int, **kwargs) -> Movie | None:
        movie = Movie.query.get(movie_id)
        if not movie:
            return None
        for key, value in kwargs.items():
            if hasattr(movie, key) and value is not None:
                setattr(movie, key, value)
        db.session.commit()
        return movie

    def delete_movie(self, movie_id: int) -> bool:
        movie = Movie.query.get(movie_id)
        if movie:
            db.session.delete(movie)
            db.session.commit()
            return True
        return False
