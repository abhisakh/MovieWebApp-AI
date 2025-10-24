"""
MovieWebApp - Flask Application Setup
-------------------------------------
Initializes Flask, SQLAlchemy, and DataManager
for managing movie data using ORM.
"""

from pathlib import Path
from flask import Flask
from data_manager import DataManager
from models import db, Movie


# ------------------------
# Flask App Initialization
# ------------------------
app = Flask(__name__)

# Define base directory using pathlib
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "movies.db"

# Ensure the /data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize ORM with app
db.init_app(app)

# Initialize DataManager
data_manager = DataManager()


# ------------------------
# Routes
# ------------------------
@app.route("/")
def home():
    """Basic test route."""
    return "Welcome to MoviWeb App!"


# ------------------------
# Main Entry Point
# ------------------------
if __name__ == "__main__":
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
        print(f"Database created at: {DB_PATH}")

    # Run Flask app
    app.run(debug=True)
