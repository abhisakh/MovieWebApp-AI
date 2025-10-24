# data_manager.py
from models import db, User, Movie


class DataManager:
    """Class to manage CRUD operations for Users and Movies."""

    def create_user(self, name: str) -> User:
        """Add a new user to the database."""
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return user

    def get_users(self) -> list[User]:
        """Return a list of all users."""
        return User.query.all()

    def get_movies(self, user_id: int) -> list[Movie]:
        """Return all movies belonging to a specific user."""
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, movie: Movie) -> Movie:
        """Add a new movie to a user's favorites after creating movie object first."""
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
