from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Model representing a user."""

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relationship to movies (one-to-many)
    movies = db.relationship(
        'Movie',
        backref='user',
        lazy=True
    )

    def __repr__(self):
        """Return string representation of the User."""
        return f"<User {self.name}>"


class Movie(db.Model):
    """Model representing a movie."""

    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=True)  # 0–10 rating

    # Foreign key linking to User
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    def __repr__(self):
        """Return string representation of the Movie."""
        return f"<Movie {self.name}>"
