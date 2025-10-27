# 🎬 MovieWebApp
<img width="1692" height="1079" alt="Screenshot 2025-10-27 at 20 46 14" src="https://github.com/user-attachments/assets/56786563-4c71-4c9e-be31-47cc620fd44a" />

MovieWebApp is a Flask-based web application that allows users to create personal movie collections. 
Users can add, update, and delete movies, fetch details from the OMDb API, and track ratings.  

---

## Features

- ✅ User management: add multiple users
-  👥 User Profiles       | Each user has a personalized movie collection.
  <img width="1692" height="1079" alt="Screenshot 2025-10-27 at 20 47 44" src="https://github.com/user-attachments/assets/23f1f1d3-7fb9-4dd5-a8a0-2c04c7dc1e13" />

- � Add Movies            | Add movies via a form; details fetched automatically from OMDb API.       
- ✏️ Rename Movies        | Rename movies directly from the movie grid using a collapsible form.      
- 🗑 Delete Movies        | Remove movies from your collection.
  <img width="1692" height="1079" alt="Screenshot 2025-10-27 at 20 48 16" src="https://github.com/user-attachments/assets/b401e983-055a-4d9b-8ac1-78dd9f1df55c" />

- ✅ OMDb API integration for automatic movie details  
- ✅ Collapsible forms for a clean UI
- ✅ Star ratings and poster display  
- <img width="964" height="721" alt="Screenshot 2025-10-27 at 20 53 36" src="https://github.com/user-attachments/assets/e5759138-c744-40d8-abe9-6692e29f118f" />
- ✅ Contact form integrated with GitHub Issues
<img width="1399" height="880" alt="Screenshot 2025-10-27 at 20 55 10" src="https://github.com/user-attachments/assets/a2079511-79b5-4aa3-bb9c-53d4d45d4450" />



---
## 🗂 Project Structure

```bash
.
├── LICENSE
├── .env                       # Stores OMDb API key and Flask secret key
├── app.py                     # Main Flask app
├── templates/
│   ├── base.html
│   └── movies.html            # Page to view and manage movies
├── static/
│   ├── scripts.js             # JS for collapsible menus
│   ├── style.css              # App styling
│   └── no-image.png           # Default poster
├── data/
│   └── movies.db              # SQLite database
├── storage/
│   └── movie_storage_sql.py   # Database operations & OMDb integration
├── requirements.txt           # Python dependencies
└── README.md
```
---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/abhisakh/MovieWebApp.git
cd MovieWebApp
```
2. **Create a virtual environment**
```bash
python3 -m venv myproject-env
source myproject-env/bin/activate  # macOS/Linux
myproject-env\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set environment variables**

Create a .env file with:
```bash
OMDB_API_KEY=<your-omdb-api-key>
FLASK_SECRET_KEY=<your-secret-key>
GITHUB_TOKEN=<your-github-token>
```

5. **Initialize the database**
```bash
flask --app app db init
flask --app app db migrate
flask --app app db upgrade
```

6. **Run the app locally**
```bash
flask --app app run --host=0.0.0.0 --port=5001 --debug
```
Open your browser at http://127.0.0.1:5001 to see it running.

## 🛠 Dependencies
Listed in requirements.txt:
```bash
# Core Flask framework
Flask==3.1.2
Werkzeug==3.1.3
Jinja2==3.1.6

# Database and migrations
Flask-SQLAlchemy==3.1.1
Flask-Migrate==4.1.0
SQLAlchemy==2.0.43

# Environment variables
python-dotenv==1.1.1

# HTTP requests (for OMDb API)
requests==2.32.4

# Optional for deployment
gunicorn==21.2.0
flask-cors==6.0.1
```

### ✨ Acknowledgments
Masterschool
- For the Codio project.
OMDb API
- for the free movies data API


## 🙋‍♂️ Author
**Abhisakh Sarma**
GitHub: [https://github.com/abhisakh](https://github.com/abhisakh)
_Contributions and feedback are always welcome!_
