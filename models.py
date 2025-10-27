# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """Model representing a user."""

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)

    # Relationship to movies (one-to-many)
    movies = db.relationship(
        'Movie',
        backref='user',
        lazy=True,
        cascade='all, delete-orphan'
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """Return string representation of the User."""
        return f"<User {self.name}>"


class Movie(db.Model):
    """Model representing a movie."""

    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    director = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False, index=True)
    poster_url = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=True)  # 0–10 rating

    # Foreign key linking to User
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """Return string representation of the Movie."""
        return f"<Movie {self.name}>"
