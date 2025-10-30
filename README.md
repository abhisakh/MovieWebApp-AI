# 🎬 MovieWebApp
<img width="1054" height="1156" alt="Screenshot 2025-10-29 at 10 26 50" src="https://github.com/user-attachments/assets/717f4551-81ed-4b7c-bb72-3c70a808358a" />

<img width="1704" height="1069" alt="Screenshot 2025-10-29 at 00 50 25" src="https://github.com/user-attachments/assets/0ae4f3ff-7450-4eb1-9b49-4f8385e5812b" />

MovieWebApp is a Flask-based web application that allows users to create personal movie collections.
Users can add, update, and delete movies, fetch details from the OMDb API, and track ratings.

---
## Online Deployed: Website link: [https://abhisakh.pythonanywhere.com/](https://abhisakh.pythonanywhere.com/)
## Features

- ✅ User management: add multiple users
-  👥 User Profiles       | Each user has a personalized movie collection.
  <img width="1704" height="1069" alt="Screenshot 2025-10-29 at 01 08 11" src="https://github.com/user-attachments/assets/06bcea27-fa29-4528-aca0-692db65babda" />

- � Add Movies            | Add movies via a form; details fetched automatically from OMDb API.
- ✏️ Rename Movies        | Rename movies directly from the movie grid using a collapsible form.
- 🗑 Delete Movies        | Remove movies from your collection.
  <img width="1704" height="1069" alt="Screenshot 2025-10-29 at 01 06 28" src="https://github.com/user-attachments/assets/86e347fa-9c23-4968-89b7-8c3c40b89e50" />


- ✅ OMDb API integration for automatic movie details
- ✅ Collapsible forms for a clean UI
- ✅ Star ratings and poster display
- <img width="964" height="721" alt="Screenshot 2025-10-27 at 20 53 36" src="https://github.com/user-attachments/assets/e5759138-c744-40d8-abe9-6692e29f118f" />
- ✅ Contact form integrated with GitHub Issues. I will receive your messeges, and will try to address them.
<img width="1399" height="880" alt="Screenshot 2025-10-27 at 20 55 10" src="https://github.com/user-attachments/assets/a2079511-79b5-4aa3-bb9c-53d4d45d4450" />

- ✅AI-Powered Suggestions
  <img width="1704" height="1069" alt="Screenshot 2025-10-29 at 01 13 34" src="https://github.com/user-attachments/assets/72956fcd-0af9-4062-8924-9697ff3ba8e9" />

- Get movie recommendations from AI using **Gemini-2.5-Flash**
- Example queries: 
  - "Best sci-fi movies of the last 5 years"  
  - "Movies directed by Christopher Nolan"  
  - "Underrated horror films from the 90s"  
  - "What to watch after Dune"
  - Feel free to formulate the question
<img width="1704" height="1069" alt="Screenshot 2025-10-29 at 01 13 49" src="https://github.com/user-attachments/assets/06b396bb-e54e-4da8-903e-fa9fd0141ef1" />


---
## 🗂 Project Structure

```bash
├── LICENSE
├── README.md
├── __init__.py
├── ai_movie_navigator.py        # AI movie helper/navigation script
├── app.py                       # Main Flask app
├── app_errors.log               # Log file for errors
├── data
│   └── movies.db                # SQLite database
├── data_manager.py              # Handles database operations
├── models.py                    # SQLAlchemy models
├── requirements.txt             # Python dependencies
├── sqlalchemy_orm_documentation.md  # ORM reference docs
├── static
│   ├── scripts.js               # JavaScript for UI interactions
│   └── style.css                # Application styling (includes fixes for forms & UI)
└── templates
    ├── 404.html                 # 404 error page
    ├── 500.html                 # 500 error page
    ├── about.html               # About page
    ├── ai_suggestions.html      # AI-powered suggestions page
    ├── app_errors.log           # (possibly misplaced, consider moving to root)
    ├── base.html                # Base template
    ├── contact.html             # Contact page
    ├── index.html               # Homepage
    └── movies.html              # Movies management page

```

---

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
Flask-Cors==3.1.3          # if using CORS in your app

# Database and migrations
Flask-SQLAlchemy==3.1.1
Flask-Migrate==4.1.0
SQLAlchemy==2.0.44         # updated minor version

# Environment variables
python-dotenv==1.1.1

# HTTP requests and API calls
requests==2.32.4
httpx==0.24.1               # for async HTTP calls if AI module uses it
urllib3==2.5.0
grpcio==1.76.0              # if using Google APIs
grpcio-status==1.71.2
google-auth==2.23.3
google-api-core==2.11.0
google-ai-generativelanguage==0.4.0
proto-plus==1.26.1
protobuf==4.24.1

# AI module dependencies
pydantic==2.7.3
pydantic-core==2.13.1
tenacity==9.1.2

# Utility / supporting packages
typing-extensions==4.15.0
typing-inspection==0.4.2
cachetools==6.2.1
blinker==1.6.2
greenlet==3.2.4
Mako==1.3.10
rsa==4.9.1
pyasn1==0.6.1
pyasn1-modules==0.4.2
h11==0.16.0
anyio==4.0.0
websockets==15.0.1

# Optional for deployment
gunicorn==21.2.0

```

---
## 💡 Detail diagram for each code block
Our movie collection project is composed of several core code blocks, each with a distinct responsibility:

- **Backend Flask App (app.py)** — The central Flask application that handles routing, request processing, and page rendering. It connects the frontend with the database through data_manager.py and models.py.

- **AI Movie Navigator (ai_movie_navigator.py)** — Handles AI-assisted movie suggestions and queries using Google Generative AI or other AI APIs. Integrates with the main app to fetch recommendations and display them in ai_suggestions.html.

- **Database Manager (data_manager.py)** — Provides an abstraction layer for all database operations. Handles CRUD operations for movies in movies.db, and ensures data integrity and proper queries.

- **Data Models (models.py)** — Defines SQLAlchemy models representing movies and related entities. These models dictate the structure, relationships, and constraints of the database.

- **Templates (templates/*.html)** — HTML files defining page structures:

- **base.html** — Provides a consistent layout and shared components (header, footer, nav bar).

- **index.html** — Homepage for general navigation.

- **movies.html** — Allows users to view, add, update, or delete movies.

- **ai_suggestions.html** — Displays AI-generated movie recommendations and search results.

- **about.html / contact.html** — Provide additional information and contact forms.

- **404.html / 500.html** — Handle error pages gracefully.

- **Static Assets (static/scripts.js & static/style.css)** —

scripts.js contains frontend logic for collapsible menus, dynamic forms, and interactive UI elements.

style.css provides styling for all HTML pages, ensuring a cinematic, user-friendly interface, including AI suggestions and movie grids.

Database (data/movies.db) — SQLite database storing all movie data, including titles, directors, years, ratings, personal notes, and metadata fetched from the OMDb API.

Requirements (**requirements.txt**) — Lists all Python dependencies needed to run the application, including Flask, SQLAlchemy, requests, and AI-related libraries for the new AI module.

---
## 🌐 🎬 app.py — Flask Application Setup Diagram

🧠 Notes:

app.py is the main Flask application for MovieWebApp.
It initializes Flask, SQLAlchemy, and DataManager, manages routes for users and movies, handles
OMDb API integration, and processes the contact form via GitHub.
All dynamic operations (DB CRUD, OMDb API) are delegated to DataManager and SQLAlchemy models.

```Bash
┌────────────────────────────────────────────────────────────────────────────┐
│ app.py — MovieWebApp Main Flask Application (Updated)                      │
├────────────────────────────────────────────────────────────────────────────┤
│ 🧭 Purpose:                                                                │
│  - Initialize Flask, SQLAlchemy, and DataManager                           │
│  - Configure database & environment variables                              │
│  - Handle routes: users, movies, AI suggestions, contact form, about page  │
│  - Perform validation, logging, and error handling                         │
│  - Delegate CRUD operations to DataManager and SQLAlchemy models           │
├────────────────────────────────────────────────────────────────────────────┤
│ ⚙️ Environment & Configurations                                            │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ load_dotenv() → load OMDB_API_KEY, FLASK_SECRET_KEY                │    │
│  │ app = Flask(__name__)                                              │    │
│  │ app.secret_key → os.environ or secrets.token_hex()                 │    │
│  │ SQLAlchemy initialized with SQLite database at data/movies.db      │    │
│  │ Logging setup: errors written to app_errors.log                    │    │
│  │ Max POST content length → 5MB                                      │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                            │
│ 🧩 Flexible Imports:                                                       │
│    - Works as package or standalone execution                              │
│    - Imports DataManager and SQLAlchemy models                             │
├────────────────────────────────────────────────────────────────────────────┤
│ 🏠 Routes Overview                                                         │
│                                                                            │
│ ["/"] → home()                                                             │
│  • Lists all users                                                         │
│  • Renders index.html                                                      │
│                                                                            │
│ ["/users"] → add_user() [POST]                                             │
│  • Add user with validation                                                │
│                                                                            │
│ ["/users/<user_id>/movies"] → user_movies() [GET]                          │
│  • Show movies for a user                                                  │
│                                                                            │
│ ["/users/<user_id>/movies"] → add_movie() [POST]                           │
│  • Add movie manually or via OMDb API                                      │
│  • Validation: year, rating, poster URL                                    │
│  • Delegates OMDb fetch to DataManager                                     │
│                                                                            │
│ ["/users/<user_id>/movies/<movie_id>/update"] → update_movie() [POST]      │
│  • Update movie details with validation                                    │
│                                                                            │
│ ["/users/<user_id>/movies/<movie_id>/delete"] → delete_movie() [POST]      │
│  • Deletes movie from DB                                                   │
│                                                                            │
│ ["/about"] → about() [GET]                                                 │
│                                                                            │
│ ["/contact"] → contact() [GET, POST]                                       │
│  • Displays contact form / POSTs message to GitHub via API                 │
│                                                                            │
│ ["/ai_suggest"] → ai_suggest() [GET, POST]                                 │
│  • AI-powered movie suggestions using Gemini                               │
│  • Enriches suggestions with OMDb data                                     │
│  • Returns list with title, director, year, rating, poster_url             │
│                                                                            │
│ ["/add_ai_movie"] → add_ai_movie() [POST]                                  │
│  • Adds AI-suggested movie to user's list                                  │
│  • Validates user, movie existence, and input fields                       │
├────────────────────────────────────────────────────────────────────────────┤
│ ⚠️ Error Handlers:                                                         │
│  - 404 → page_not_found()                                                  │
│  - 500 → internal_server_error()                                           │
│  • Both render templates with flash messages                               │
├────────────────────────────────────────────────────────────────────────────┤
│ 🧩 Context Processor                                                       │
│  - inject_globals() adds:                                                  │
│      • current_year → datetime.now().year                                  │
│      • users → data_manager.get_users()                                    │
│      • current_user → highlights user currently being viewed               │
├────────────────────────────────────────────────────────────────────────────┤
│ 🔄 Data Flow Summary                                                       │
│                                                                            │
│ [User Browser]                                                             │
│       ↓ GET/POST Requests                                                  │
│ app.py Routes → Validation → DataManager/SQLAlchemy                        │
│       ↓                                                                    │
│ DataManager → db.session → Movie/User models → SQLite movies.db            │
│       ↓ Response                                                           │
│ app.py → render_template → index.html/movies.html/ai_suggestions.html/...  │
│       ↓                                                                    │
│ Browser → Displays updated DOM                                             │
│                                                                            │
│ 🌐 Contact Form Flow                                                       │
│ [Browser POST /contact] → app.py → save_contact_to_github()                │
│       ↓                                                                    │
│ GitHub API → Issue created in MovieWebApp repo → Success/Failure flash     │
├────────────────────────────────────────────────────────────────────────────┤
│ ⚡ Execution Entry Point                                                    │
│  if __name__ == "__main__":                                                │
│      db.create_all() → initialize SQLite DB                                │
│      app.run(host="0.0.0.0", port=5001, debug=True)                        │
└────────────────────────────────────────────────────────────────────────────┘

```
## 🧩 ai_movie_navigator.py— Project Structure Diagram
```Bash
┌────────────────────────────────────────────────────────────────────────────┐
│ ai_movie_navigator.py — AI Movie Suggestions via Gemini API                │
├────────────────────────────────────────────────────────────────────────────┤
│ 🧭 Purpose:                                                                │
│  - Provide structured movie recommendations using Gemini API               │
│  - Return suggestions in JSON adhering to MovieSuggestionList schema       │
│  - Handle errors, empty responses, and API connectivity issues             │
├────────────────────────────────────────────────────────────────────────────┤
│ ⚙️ Environment & Configurations                                            │
│  - load_dotenv() → load GEMINI_API_KEY                                     │
│  - client = genai.Client(api_key=GEMINI_API_KEY) if API key exists         │
│  - Prints diagnostic message if API key is missing                         │
├────────────────────────────────────────────────────────────────────────────┤
│ 🧩 Data Models (Pydantic)                                                  │
│  • MovieSuggestion:                                                        │
│      - title: str                                                          │
│      - year: int (0 if unknown)                                            │
│      - director: str ('Unknown' if missing)                                │
│                                                                            │
│  • MovieSuggestionList:                                                    │
│      - suggestions: list of 5 MovieSuggestion objects                      │
├────────────────────────────────────────────────────────────────────────────┤
│ ⚡ Main Function: get_ai_movie_suggestions(query, max_suggestions=5)        │
│                                                                            │
│ 1️⃣ Validates API client and query                                          │
│ 2️⃣ Constructs system_instruction & prompt for Gemini                       │
│ 3️⃣ Configures GenerateContentConfig (response_schema=MovieSuggestionList)  │
│ 4️⃣ Calls Gemini API: client.models.generate_content(...)                   │
│ 5️⃣ Extracts JSON block from response.text                                  │
│ 6️⃣ Parses JSON → suggestions list                                          │
│ 7️⃣ Returns (suggestions, model_name)                                       │
│                                                                            │
│ 🔹 Error Handling:                                                         │
│  - Empty response text → logs error & return ([], "Error")                 │
│  - JSON parse failure → logs error & return ([], "Error")                  │
│  - API/network exceptions → logs & prints diagnostic → return ([], "Error")│
├────────────────────────────────────────────────────────────────────────────┤
│ 🧪 Test Block (Optional)                                                   │
│  - Runs a sample query when executed as __main__                           │
│  - Prints list of movie suggestion dicts with titles, years, directors     │
├────────────────────────────────────────────────────────────────────────────┤
│ 🔄 Data Flow Summary                                                       │
│ [Flask app POST /ai_suggest] → query string                                │
│       ↓                                                                    │
│ ai_movie_navigator.get_ai_movie_suggestions(query)                         │
│       ↓                                                                    │
│ Gemini API → JSON response → parsed dict list                              │
│       ↓                                                                    │
│ Flask receives enriched suggestions → renders ai_suggestions.html          │
└────────────────────────────────────────────────────────────────────────────┘

```

## 🌐 🎬 data_manager.py — Flask Application Setup Diagram
```Bash
+-----------------------------------------------------+
|                     DataManager                     |
+-----------------------------------------------------+
| Handles CRUD for Users and Movies                   |
| Integrates OMDb API for fetching movie details      |
+-----------------------------------------------------+
|  USER OPERATIONS                                    |
|  -----------------                                  |
|  + create_user(name) -> User                        |
|      - Adds a new user to the DB                    |
|  + get_users() -> list[User]                        |
|      - Returns all users                            |
+-----------------------------------------------------+
|  MOVIE OPERATIONS                                   |
|  -----------------                                  |
|  + get_movies(user_id) -> list[Movie]               |
|      - Fetches movies for a user                    |
|  + add_movie(movie: Movie) -> Movie                 |
|      - Adds movie object to DB                      |
|  + update_movie(movie_id, **kwargs) -> Movie|None   |
|      - Dynamically updates movie fields             |
|  + delete_movie(movie_id) -> bool                   |
|      - Deletes a movie by ID                        |
+-----------------------------------------------------+
|  OMDb INTEGRATION                                   |
|  -----------------                                  |
|  + add_movie_from_omdb(movie_name, user_id)         |
|      -> Returns (Movie|None, suggestions[], added)  |
|      - Checks DB first                              |
|      - Tries exact match with OMDb API              |
|      - Returns suggestions if exact match fails     |
|  - _fetch_movie_by_title(title, user_id) -> Movie   |
|      - Fetches movie details by title from OMDb     |
|  - _fetch_movie_by_imdb_id(imdb_id, user_id) -> Movie |
|      - Fetches movie details by IMDb ID             |
|  - _create_movie_from_data(data, user_id) -> Movie  |
|      - Creates and commits Movie object from OMDb   |
+-----------------------------------------------------+
|  DEPENDENCIES                                       |
|  -----------------                                  |
|  - db (SQLAlchemy)                                  |
|  - User, Movie models                               |
|  - requests (for OMDb API)                          |
|  - dotenv (for OMDB_API_KEY)                        |
+-----------------------------------------------------+

```
## 🌐 🎬 models.py — Flask Application Setup Diagram
```Bash
+---------------------------------------+
|                User                   |
+---------------------------------------+
| Table: user                           |
+---------------------------------------+
| id : Integer [PK]                     |
|    - Primary key                      |
| name : String(100) [Not Null, Indexed]|
|    - User's name                      |
| created_at : DateTime                 |
|    - Default: datetime.utcnow         |
+---------------------------------------+
| Relationships:                        |
| movies : List[Movie]                  |
|    - One-to-many with Movie           |
|    - backref='user'                   |
|    - lazy=True                        |
|    - cascade='all, delete-orphan'     |
+---------------------------------------+
| Methods:                              |
| __repr__() -> str                     |
|    - Returns "<User {name}>"          |
+---------------------------------------+


+----------------------------------------+
|                Movie                   |
+----------------------------------------+
| Table: movie                           |
+----------------------------------------+
| id : Integer [PK]                      |
|    - Primary key                       |
| name : String(100) [Not Null, Indexed] |
|    - Movie title                       |
| director : String(100) [Not Null]      |
|    - Director name                     |
| year : Integer [Not Null, Indexed]     |
|    - Release year                      |
| poster_url : String(255) [Not Null]    |
|    - URL to movie poster               |
| rating : Float [Nullable]              |
|    - IMDb rating (0–10)                |
| user_id : Integer [FK -> user.id]      |
|    - Foreign key to User               |
| created_at : DateTime                  |
|    - Default: datetime.utcnow          |
+----------------------------------------+
| Relationships:                         |
| user : User                            |
|    - Many-to-one with User             |
+----------------------------------------+
| Methods:                               |
| __repr__() -> str                      |
|    - Returns "<Movie {name}>"          |
+----------------------------------------+
```


## 🧩 base.html — Project Structure Diagram
```Bash
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ base.html — Main Layout Template                                                                                                                               │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ <head>                                                                                                                                                         │
│  • Metadata (charset, viewport)                                                                                                                                │
│  • Title block: {% block title %}MovieWeb App{% endblock %}                                                                                                    │
│  • <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">                                                                                │
│                                                                                                                                                                │
│ <body>                                                                                                                                                         │
│  ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐  │   
│  │ <header>                                                                                                                                                 │  │
│  │  • Left reel: 🎞️ div.reel-left                                                                                                                           │  │
│  │  • Header center: h1 + nav                                                                                                                               │  │
│  │      ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐  │  │
│  │      │ h1: Title "MovieWeb App" + rainbow emojis 🌈                                                                                                   │  │  │
│  │      │ <nav class="nav-bar">                                                                                                                          │  │  │
│  │      │   • <ul>                                                                                                                                       │  │  │
│  │      │       <li class="{{ 'active' if request.path == url_for('home') else '' }}"><a href="{{ url_for('home') }}">Home</a></li>                      │  │  │
│  │      │       <li class="{{ 'active' if request.path == url_for('about') else '' }}"><a href="{{ url_for('about') }}">About</a></li>                   │  │  │
│  │      │       <li class="{{ 'active' if request.path == url_for('contact') else '' }}"><a href="{{ url_for('contact') }}">Contact</a></li>             │  │  │
│  │      │       <li class="{{ 'active' if request.path == url_for('ai_suggest') else '' }}"><a href="{{ url_for('ai_suggest') }}">AI Suggestions</a></li>│  │  │
│  │      │   </ul>                                                                                                                                        │  │  │
│  │      └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘  │  │
│  │  • Right reel: 🎞️ div.reel-right                                                                                                                         │  │
│  └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                                                                                                │
│  ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐  │
│  │ <div class="wrapper">                                                                                                                                    │  │
│  │                                                                                                                                                          │  │
│  │  ┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐ │  │
│  │  │ Left Sidebar (users)                                                                                                                                │ │  │
│  │  │ {% if request.endpoint != 'home' %}                                                                                                                 │ │  │
│  │  │   • <h3>🎬 Users</h3>                                                                                                                               │ │  │
│  │  │   • <ul>                                                                                                                                            │ │  │
│  │  │       {% set current_user = current_user or None %}                                                                                                 │ │  │
│  │  │       {% for user in users %}                                                                                                                       │ │  │
│  │  │         <li class="{% if current_user and user.id == current_user.id %}active{% endif %}">                                                          │ │  │
│  │  │           <a href="{{ url_for('user_movies', user_id=user.id) }}">{{ user.name }}</a>                                                               │ │  │
│  │  │         </li>                                                                                                                                       │ │  │
│  │  │       {% endfor %}                                                                                                                                  │ │  │
│  │  │   </ul>                                                                                                                                             │ │  │
│  │  │ {% else %}                                                                                                                                          │ │  │
│  │  │   <div class="empty-sidebar"></div>                                                                                                                 │ │  │
│  │  │ {% endif %}                                                                                                                                         │ │  │
│  │  └─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘ │  │
│  │                                                                                                                                                          │  │
│  │  ┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐ │  │
│  │  │ Main Content                                                                                                                                        │ │  │
│  │  │ {% if request.endpoint != 'home' %}                                                                                                                 │ │  │
│  │  │   • Back to Home Button: <a href="{{ url_for('home') }}">🏠 ← Back</a>                                                                              │ │  │
│  │  │ {% endif %}                                                                                                                                         │ │  │
│  │  │ {% block content %}{% endblock %}                                                                                                                   │ │  │
│  │  └─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘ │  │
│  │                                                                                                                                                          │  │
│  │  ┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐ │  │
│  │  │ Right Sidebar (empty)                                                                                                                               │ │  │
│  │  │ <div class="empty-sidebar"></div>                                                                                                                   │ │  │
│  │  └─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                                                                                                │
│  ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐  │
│  │ Flash Messages                                                                                                                                           │  │
│  │ {% with messages = get_flashed_messages(with_categories=true) %}                                                                                         │  │
│  │   {% if messages %}                                                                                                                                      │  │
│  │     • <div class="flash-messages">                                                                                                                       │  │
│  │     • {% for category, msg in messages %}                                                                                                                │  │
│  │         <div class="flash {{ category }}">{{ msg }}</div>                                                                                                │  │
│  │       {% endfor %}                                                                                                                                       │  │
│  │     </div>                                                                                                                                               │  │
│  │   {% endif %}                                                                                                                                            │  │
│  │ {% endwith %}                                                                                                                                            │  │
│  └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                                                                                                │
│  <footer> &copy; {{ current_year }} MovieWeb App </footer>                                                                                                     │
│                                                                                                                                                                │
│  <script src="{{ url_for('static', filename='scripts.js') }}"></script>                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘


```

## 🧩 Index.html — Project Structure Diagram

```Bash
┌───────────────────────────────────────────────────────────────────────────────────┐
│ home.html                                                                         │
├───────────────────────────────────────────────────────────────────────────────────┤
│ {% extends "base.html" %}                                                         │
│ {% block title %}Home - MovieWeb{% endblock %}                                    │
│                                                                                   │
│ {% block content %}                                                               │
│  ┌───────────────────────────────────────────────────────────────────────────┐    │
│  │ <section class="users-section">                                           │    │
│  │                                                                           │    │
│  │  • <h2>🧑‍🎤 All Users</h2>                                                  │    │
│  │                                                                           │    │
│  │  ┌───────────────────────────────────────────────────────────────────┐    │    │
│  │  │ Users List                                                        │    │    │
│  │  │ {% if users %}                                                    │    │    │
│  │  │   <ul class="user-list">                                          │    │    │
│  │  │     {% for user in users %}                                       │    │    │
│  │  │       <li>                                                        │    │    │
│  │  │         <a href="{{ url_for('user_movies', user_id=user.id) }}">  │    │    │
│  │  │           🎬 {{ user.name }}                                      │    │    │
│  │  │         </a>                                                      │    │    │
│  │  │       </li>                                                       │    │    │
│  │  │     {% endfor %}                                                  │    │    │
│  │  │   </ul>                                                           │    │    │
│  │  │ {% else %}                                                        │    │    │
│  │  │   <p>No users found. Add a new user below!</p>                    │    │    │
│  │  │ {% endif %}                                                       │    │    │
│  │  └───────────────────────────────────────────────────────────────────┘    │    │
│  │                                                                           │    │
│  │  <hr>                                                                     │    │
│  │                                                                           │    │
│  │  ┌────────────────────────────────────────────────────────────┐           │    │
│  │  │ Add New User Form                                          │           │    │
│  │  │ <form action="{{ url_for('add_user') }}" method="POST">    │           │    │
│  │  │   • Input: User Name (required)                            │           │    │
│  │  │   • Button: Add User                                       │           │    │
│  │  └────────────────────────────────────────────────────────────┘           │    │
│  └───────────────────────────────────────────────────────────────────────────┘    │
│ {% endblock %}                                                                    │
└───────────────────────────────────────────────────────────────────────────────────┘

```

## 🧩 movies.html — Project Structure Diagram
```Bash
┌────────────────────────────────────────────────────────────────────────────────────────────┐
│ movies.html                                                                                │
├────────────────────────────────────────────────────────────────────────────────────────────┤
│ {% extends "base.html" %}                                                                  │
│ {% block title %}{{ user.name }}'s Movies{% endblock %}                                    │
│                                                                                            │
│ {% block content %}                                                                        │
│  ┌────────────────────────────────────────────────────────────────────────────────────┐    │
│  │ <section class="movies-section">                                                   │    │
│  │                                                                                    │    │
│  │  • <h2>🎬 {{ user.name }}’s Favorite Movies</h2>                                   │    │
│  │                                                                                    │    │
│  │  ┌──────────────────────────────────────────────────────────────┐                  │    │
│  │  │ Add Movie Toggle Button                                      │                  │    │
│  │  │ <button id="toggleAddMovie">➕ Add Movie</button>            │                  │    │
│  │  └──────────────────────────────────────────────────────────────┘                  │    │
│  │                                                                                    │    │
│  │  ┌────────────────────────────────────────────────────────────────────────────┐    │    │
│  │  │ Collapsible Add Movie Form                                                 │    │    │
│  │  │ <form method="POST" action="{{ url_for('add_movie', user_id=user.id) }}">  │    │    │
│  │  │  • Input: Movie Name (required)                                            │    │    │
│  │  │  • Input: Director (optional)                                              │    │    │
│  │  │  • Input: Year (number, min 1888, max current_year+1)                      │    │    │
│  │  │  • Input: Rating (0–10, optional)                                          │    │    │
│  │  │  • Buttons: Submit (🔍 Search & Add), Cancel (✖)                           │    │    │
│  │  │  • Info: Auto-fetch from OMDb                                              │    │    │
│  │  └────────────────────────────────────────────────────────────────────────────┘    │    │
│  │                                                                                    │    │
│  │  <hr>                                                                              │    │
│  │                                                                                    │    │
│  │  ┌────────────────────────────────────────────────────────────────────────────┐    │    │
│  │  │ Movies Grid                                                                │    │    │
│  │  │ {% if movies %}                                                            │    │    │
│  │  │   {% for movie in movies %}                                                │    │    │
│  │  │                                                                            │    │    │
│  │  │   ┌──────────────────────────────────────────────────────┐                 │    │    │
│  │  │   │ Movie Card                                           │                 │    │    │
│  │  │   │ • Poster Image (with fallback if missing)            │                 │    │    │
│  │  │   │ • Movie Details:                                     │                 │    │    │
│  │  │   │     - Name                                           │                 │    │    │
│  │  │   │     - Director                                       │                 │    │    │
│  │  │   │     - Year                                           │                 │    │    │
│  │  │   │     - Rating (displayed as stars & numeric)          │                 │    │    │
│  │  │   │ • Toggle Update Button: ✏️ Rename                    │                 │    │    │
│  │  │   │ • Collapsible Update Form                            │                 │    │    │
│  │  │   │     - Input: New Title                               │                 │    │    │
│  │  │   │     - Buttons: Update, Cancel                        │                 │    │    │
│  │  │   │ • Delete Form                                        │                 │    │    │
│  │  │   │     - Button: Delete                                 │                 │    │    │
│  │  │   └──────────────────────────────────────────────────────┘                 │    │    │
│  │  │ {% endfor %}                                                               │    │    │
│  │  │ {% else %}                                                                 │    │    │
│  │  │   <p>No movies found message + prompt to add movie</p>                     │    │    │
│  │  │ {% endif %}                                                                │    │    │
│  │  └────────────────────────────────────────────────────────────────────────────┘    │    │
│  └────────────────────────────────────────────────────────────────────────────────────┘    │
│ {% endblock %}                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────┘


```
## 🧩 contact.html — Project Structure Diagram
```Bash
┌──────────────────────────────────────────────────────────────────────────────────┐
│ contact.html                                                                     │
├──────────────────────────────────────────────────────────────────────────────────┤
│ {% extends "base.html" %}                                                        │
│ {% block title %}Contact Us{% endblock %}                                        │
│                                                                                  │
│ {% block content %}                                                              │
│  ┌──────────────────────────────────────────────────────────────────────────┐    │
│  │ <section class="contact-section">                                        │    │
│  │                                                                          │    │
│  │  • <h2>Contact Us 📬</h2>                                                │    │
│  │  • <p>Prompt for questions, suggestions, or feedback</p>                 │    │
│  │                                                                          │    │
│  │  ┌──────────────────────────────────────────────────────────────────┐    │    │
│  │  │ Flash Messages                                                   │    │    │
│  │  │ {% with messages = get_flashed_messages(with_categories=true) %} │    │    │
│  │  │   {% if messages %}                                              │    │    │
│  │  │     <ul class="flash-messages">                                  │    │    │
│  │  │       {% for category, message in messages %}                    │    │    │
│  │  │         <li class="{{ category }}">{{ message }}</li>            │    │    │
│  │  │       {% endfor %}                                               │    │    │
│  │  │     </ul>                                                        │    │    │
│  │  │   {% endif %}                                                    │    │    │
│  │  │ {% endwith %}                                                    │    │    │
│  │  └──────────────────────────────────────────────────────────────────┘    │    │
│  │                                                                          │    │
│  │  ┌──────────────────────────────────────────────────────────────────┐    │    │
│  │  │ Contact Form                                                     │    │    │
│  │  │ <form action="{{ url_for('contact') }}" method="POST">           │    │    │
│  │  │  • Input: Name (required)                                        │    │    │
│  │  │  • Input: Email (required)                                       │    │    │
│  │  │  • Textarea: Message (required)                                  │    │    │
│  │  │  • Button: Send Message                                          │    │    │
│  │  └──────────────────────────────────────────────────────────────────┘    │    │
│  └──────────────────────────────────────────────────────────────────────────┘    │
│ {% endblock %}                                                                   │
└──────────────────────────────────────────────────────────────────────────────────┘

```
## 🧩 about.html — Project Structure Diagram

```Bash
┌───────────────────────────────────────────────────────────────────────────────┐
│ about.html                                                                    │
├───────────────────────────────────────────────────────────────────────────────┤
│ {% extends "base.html" %}                                                     │
│ {% block title %}About Us{% endblock %}                                       │
│                                                                               │
│ {% block content %}                                                           │
│  ┌───────────────────────────────────────────────────────────────────────┐    │
│  │ <section class="about-section">                                       │    │
│  │                                                                       │    │
│  │  • <h2>About MovieWebApp 🎬</h2>                                      │    │
│  │                                                                       │    │
│  │  • <p>Welcome message explaining the purpose of the platform.</p>     │    │
│  │                                                                       │    │
│  │  • <p>Mission statement about making movie management fun & easy.</p> │    │
│  │                                                                       │    │
│  │  • <p>Introduction to main features:</p>                              │    │
│  │                                                                       │    │
│  │  ┌──────────────────────────────────────────────────────────────┐     │    │
│  │  │ Features List                                                │     │    │
│  │  │ <ul>                                                         │     │    │
│  │  │   <li>Personalized movie lists</li>                          │     │    │
│  │  │   <li>Automatic OMDb integration</li>                        │     │    │
│  │  │   <li>Rating and review management</li>                      │     │    │
│  │  │   <li>Easy editing and deleting of movies</li>               │     │    │
│  │  │ </ul>                                                        │     │    │
│  │  └──────────────────────────────────────────────────────────────┘     │    │
│  └───────────────────────────────────────────────────────────────────────┘    │
│ {% endblock %}                                                                │
└───────────────────────────────────────────────────────────────────────────────┘


```

## 🧩ai_suggestions.html
```Bash
┌─────────────────────────────────────────────────────────────────────────────────┐
│ ai_suggest.html — AI Movie Suggestions Page                                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│ {% extends "base.html" %}                                                       │
│ {% block title %}AI Movie Suggestions{% endblock %}                             │
│                                                                                 │
│ {% block content %}                                                             │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ <div class="container mt-4 ai-search-area">                               │  │
│  │                                                                           │  │
│  │  • Page Title: 🎬 AI Movie Suggestions                                    │  │
│  │                                                                           │  │
│  │  ┌─────────────────────────────────────────────────────────────────────┐  │  │
│  │  │ Search Form (POST /ai_suggest)                                      │  │  │
│  │  │ id="ai-search-form"                                                 │  │  │
│  │  │   • Input: text field (movie_query)                                 │  │  │
│  │  │   • Submit Button: Get Suggestions                                  │  │  │
│  │  │   • Loading Spinner (id="loading-indicator")                        │  │  │
│  │  │   • Example Queries (ul.list-unstyled.flex-wrap)                    │  │  │
│  │  └─────────────────────────────────────────────────────────────────────┘  │  │
│  │                                                                           │  │
│  │  {% if query %}                                                           │  │
│  │    • Display search term: Results for "<query>"                           │  │
│  │  {% endif %}                                                              │  │
│  │                                                                           │  │
│  │  {% if model_name %}                                                      │  │
│  │    • Model used: <strong>{{ model_name }}</strong>                        │  │
│  │  {% endif %}                                                              │  │
│  │                                                                           │  │
│  │  {% if suggestions %}                                                     │  │
│  │   ┌─────────────────────────────────────────────────────────────────────┐ │  │
│  │   │ Add to User Selector (dropdown)                                     │ │  │
│  │   │ id="target_user", pre-select current_user                           │ │  │
│  │   └─────────────────────────────────────────────────────────────────────┘ │  │
│  │                                                                           │  │
│  │   <ul class="list-group shadow-sm">                                       │  │
│  │   {% for movie in suggestions %}                                          │  │
│  │    ┌───────────────────────────────────────────────────────────────────┐  │  │
│  │    │ <li class="list-group-item">                                      │  │  │
│  │    │   • Content wrapper (flex)                                        │  │  │
│  │    │       • Poster image (if movie.poster_url)                        │  │  │
│  │    │       • Title, Year, Director, Star Rating                        │  │  │
│  │    │   • Form to add movie to list (POST /add_ai_movie)                │  │  │
│  │    │       • Hidden fields: user_id, movie_name, director, year, rating│  │  │
│  │    │       • Hidden: poster_url                                        │  │  │
│  │    │       • Submit button: Add to List                                │  │  │
│  │    └───────────────────────────────────────────────────────────────────┘  │  │
│  │   {% endfor %}                                                            │  │
│  │   </ul>                                                                   │  │
│  │  {% elif query %}                                                         │  │
│  │   • Alert: ❌ No AI suggestions found.                                    │  │
│  │  {% endif %}                                                              │  │
│  │                                                                           │  │
│  │  <hr class="my-4">                                                        │  │
│  │  • Footer note: Powered by Google Gemini                                  │  │
│  │  <div class="mb-5"></div>                                                 │  │
│  │                                                                           │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│ {% endblock %}                                                                  │
│                                                                                 │
│ {% block scripts %}                                                             │
│  <script src="{{ url_for('static', filename='scripts.js') }}"></script>         │
│ {% endblock %}                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

```

## 🧩 scripts.js — Project Structure Diagram

```Bash
┌─────────────────────────────────────────────────────────────────────────────────────┐
│ scripts.js                                                                          │
├─────────────────────────────────────────────────────────────────────────────────────┤
│ document.addEventListener('DOMContentLoaded', () => {                               │
│                                                                                     │
│  // -----------------------------                                                   │
│  // Flash Messages Auto-Dismiss                                                     │
│  // -----------------------------                                                   │
│  ┌────────────────────────────────────────────────────────────────────┐             │
│  │ const flashes = document.querySelectorAll(".flash")                │             │
│  │ flashes.forEach(flash => {                                         │             │
│  │     setTimeout(() => {                                             │             │
│  │         flash.classList.add("fade-out")                            │             │
│  │         setTimeout(() => flash.remove(), 1000)                     │             │
│  │     }, 4000)                                                       │             │
│  │ })                                                                 │             │
│  └────────────────────────────────────────────────────────────────────┘             │
│  → Automatically fades out flash messages 4 seconds after display                   │
│                                                                                     │
│  // -----------------------------                                                   │
│  // Add Movie Form Toggle                                                           │
│  // -----------------------------                                                   │
│  ┌────────────────────────────────────────────────────────────────────┐             │
│  │ const toggleAddBtn = document.getElementById("toggleAddMovie")     │             │
│  │ const addFormContainer = document.getElementById("addMovieForm")   │             │
│  │ const cancelAddBtn = document.getElementById("cancelAddMovie")     │             │
│  │                                                                    │             │
│  │ toggleAddBtn.addEventListener("click", () => {                     │             │
│  │     addFormContainer.classList.toggle("open")                      │             │
│  │     toggleAddBtn.textContent = ...                                 │             │
│  │ })                                                                 │             │
│  │                                                                    │             │
│  │ cancelAddBtn.addEventListener("click", () => {                     │             │
│  │     addFormContainer.classList.remove("open")                      │             │
│  │     toggleAddBtn.textContent = "➕ Add Movie"                      │             │
│  │ })                                                                 │             │
│  └────────────────────────────────────────────────────────────────────┘             │
│  → Opens/closes "Add Movie" form and updates button text                            │
│                                                                                     │
│  // -----------------------------                                                   │
│  // Update Movie Form Toggle                                                        │
│  // -----------------------------                                                   │
│  ┌─────────────────────────────────────────────────────────────────────────────┐    │
│  │ const updateButtons = document.querySelectorAll('.toggle-update-btn')       │    │
│  │ updateButtons.forEach(btn => {                                              │    │
│  │     btn.addEventListener('click', () => {                                   │    │
│  │         const formContainer = btn.nextElementSibling                        │    │
│  │         formContainer.classList.toggle('open')                              │    │
│  │     })                                                                      │    │
│  │ })                                                                          │    │
│  │                                                                             │    │
│  │ const cancelUpdateButtons = document.querySelectorAll('.cancel-update-btn') │    │
│  │ cancelUpdateButtons.forEach(btn => {                                        │    │
│  │     btn.addEventListener('click', () => {                                   │    │
│  │         const formContainer = btn.closest('.collapsible-update-form')       │    │
│  │         formContainer.classList.remove('open')                              │    │
│  │     })                                                                      │    │
│  │ })                                                                          │    │
│  └─────────────────────────────────────────────────────────────────────────────┘    │
│  → Toggles "Update Movie" forms per movie card, with cancel button                  │
│                                                                                     │
│  // -----------------------------                                                   │
│  // AI Movie Suggestions Handling                                                   │
│  // -----------------------------                                                   │
│  ┌─────────────────────────────────────────────────────────────────────────────┐    │
│  │ const userSelect = document.getElementById('target_user')                   │    │
│  │ const userIdInputs = document.querySelectorAll('.user-id-input')            │    │
│  │ const searchForm = document.getElementById('ai-search-form')                │    │
│  │ const searchButton = document.getElementById('search-button')               │    │
│  │ const loadingIndicator = document.getElementById('loading-indicator')       │    │
│  │                                                                             │    │
│  │ function updateForms() {                                                    │    │
│  │     const selectedUserId = userSelect ? userSelect.value : null             │    │
│  │     if (selectedUserId) {                                                   │    │
│  │         userIdInputs.forEach(input => { input.value = selectedUserId })     │    │
│  │     }                                                                       │    │
│  │ }                                                                           │    │
│  │                                                                             │    │
│  │ if (userSelect) {                                                           │    │
│  │     updateForms()                                                           │    │
│  │     userSelect.addEventListener('change', updateForms)                      │    │
│  │ }                                                                           │    │
│  │                                                                             │    │
│  │ if (searchForm && searchButton && loadingIndicator) {                       │    │
│  │     searchForm.addEventListener('submit', () => {                           │    │
│  │         searchButton.disabled = true                                        │    │
│  │         searchButton.innerHTML = '<i class="bi bi-search"></i> Searching...'│    │
│  │         loadingIndicator.style.display = 'block'                            │    │
│  │     })                                                                      │    │
│  │ }                                                                           │    │
│  └─────────────────────────────────────────────────────────────────────────────┘    │
│  → Handles AI search form submit: updates hidden user_id inputs, shows spinner      │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘


```
## 🎨 style.css — Detailed ANSI Block Diagram

```Bash
┌────────────────────────────────────────────────────────────┐
│ 🌐 GLOBAL STYLES — Modern Cinematic Theme                  │
├────────────────────────────────────────────────────────────┤
│ *                     → Universal Reset (margin, padding)  │
│ body                  → Full-screen dark gradient layout   │
│ body::before          → Overlay with soft glow texture     │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 🏠 BACK TO HOME BUTTON                                     │
├────────────────────────────────────────────────────────────┤
│ .back-home-container    → Wrapper                          │
│ .back-home-btn          → Green button (rounded, hover fx) │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 🎬 HEADER — Neon Cinema Title Bar                          │
├────────────────────────────────────────────────────────────┤
│ header                 → Sticky bar (gradient bg, shadow)  │
│ ├─ .reel-left/.reel-right  → Spinning reels (animation)    │
│ ├─ .header-center       → Flex-centered title layout       │
│ ├─ h1.title-text        → Gradient neon movie title        │
│ └─ @keyframes reel-spin & neon-glow → Animation effects    │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 🧭 NAV BAR — Neon Links + Glowing Separators               │
├────────────────────────────────────────────────────────────┤
│ .nav-bar               → Center-aligned navigation bar     │
│ ├─ ul, li              → Horizontal flex list              │
│ ├─ li + li::before     → Neon divider between links        │
│ └─ a:hover             → Cyan glow hover effect            │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ ⚡ FLASH MESSAGES                                           │
├────────────────────────────────────────────────────────────┤
│ .flash-messages         → Fixed top position               │
│ ├─ .flash.success        → Green glow background           │
│ ├─ .flash.error          → Red glow background             │
│ ├─ .flash.info           → Blue glow background            │
│ └─ .fade-out             → Auto dismiss animation          │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 🧭 MAIN WRAPPER STRUCTURE                                  │
├────────────────────────────────────────────────────────────┤
│ .wrapper              → Flex container                     │
│ ├─ aside              → Sidebar (left panel)               │
│ └─ main               → Main content area                  │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 🎞️ SIDEBAR — User Selector Panel                           │
├────────────────────────────────────────────────────────────┤
│ aside                 → Dark gradient panel                │
│ ├─ h3                 → Gold glowing heading               │
│ ├─ ul li a            → User links w/ 🎥 icon              │
│ │   ├─ hover          → Cyan glow + slide animation        │
│ │   └─ active         → Gold highlight state               │
│ └─ ::before           → Subtle background glow layer       │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 📄 MAIN CONTENT — Movies & Users Display                   │
├────────────────────────────────────────────────────────────┤
│ main                  → Central area                       │
│ ├─ h2 / h3            → Neon-glow section headers          │
│ ├─ .user-list         → List of users                      │
│ │   ├─ li             → Neon cards w/ hover effect         │
│ │   └─ a:hover        → Text glow + color change           │
│ └─ .movies-grid       → Responsive movie card layout       │
│     ├─ .movie-card    → Movie thumbnail + details          │
│     │   ├─ img        → Poster image w/ border             │
│     │   ├─ .movie-details → Info & rating section          │
│     │   ├─ .update-form / .delete-form buttons             │
│     │   └─ hover       → Pulsing glow animation            │
│     └─ @keyframes pulse-glow → Animation definition        │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 🧾 FORMS — Input & Button Styling                          │
├────────────────────────────────────────────────────────────┤
│ form                 → Flex column layout                  │
│ input[type=text|num] → Dark field + glowing focus border   │
│ button               → Gradient background (purple tones)  │
│ button:hover         → Scale-up + lighter gradient         │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 🎬 COLLAPSIBLE FORMS (Add / Update Movie)                  │
├────────────────────────────────────────────────────────────┤
│ .toggle-btn            → Trigger button for form toggle    │
│ .collapsible-form      → Hidden by default (max-height: 0) │
│ .collapsible-form.open → Smooth expand transition          │
│ .cancel-btn            → Yellow-bordered cancel button     │
│ .cancel-btn:hover      → Inverted yellow-black style       │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 🎬 INLINE UPDATE BUTTONS                                   │
├────────────────────────────────────────────────────────────┤
│ .toggle-update-btn     → Inline edit toggle button         │
│ .toggle-update-btn:hover → Yellow glow highlight           │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ ⭐ STAR RATINGS                                            │
├────────────────────────────────────────────────────────────┤
│ .star                → Gold text w/ glowing animation      │
│ @keyframes star-glow → Pulsing light effect                │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ ⚓ FOOTER — Gradient & Glow Border                          │
├────────────────────────────────────────────────────────────┤
│ footer               → Blue-purple gradient + shadow       │
│ footer::before       → RGB neon line (top border)          │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 📱 RESPONSIVE DESIGN (≤768px)                              │
├────────────────────────────────────────────────────────────┤
│ .wrapper             → Column layout on small screens      │
│ aside                → Full width, border-bottom only      │
│ main                 → Reduced padding                     │
│ header h1            → Smaller title font size             │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│ 📱 ABOUT & CONTACT PAGES                                   │
├────────────────────────────────────────────────────────────┤
│ .about-section         → Centered text block               │
│ .contact-form div      → Vertical spacing between inputs   │
│ .contact-form input/textarea → Light-bordered fields       │
│ .contact-form button   → Green CTA + hover effect          │
└────────────────────────────────────────────────────────────┘

```
## 🧩 CSS Functional Flow (Simplified Overview)

```Bash
GLOBAL STYLES
│
├── HEADER (Reels + Title + Nav)
│
├── FLASH MESSAGES (Overlay Alerts)
│
├── WRAPPER
│   ├── SIDEBAR (User/Links)
│   └── MAIN CONTENT
│       ├── USERS LIST
│       ├── MOVIES GRID
│       └── FORMS (Add/Update)
│
└── FOOTER (Gradient Glow)
```

## 💡 Future Enhancements
## 1. Medium-Term Goals (3–6 months)

**Focus:** Enhance features and interactivity.

### 🎬 User Authentication
- Add login/register functionality (Flask-Login).
- Make movie lists private by default; allow sharing.

### 📊 Movie Statistics & Sorting
- Filter movies by rating, year, or director.
- Add charts (e.g., most-watched director, average rating).

### 🌐 External API Enhancements
- Fetch trailers or reviews from YouTube / TMDb.
- Auto-update missing movie posters or data.

### 🗂 Search & Pagination
- Implement search by movie name or director.
- Paginate user’s movie lists for large collections.

---

## 2. Long-Term Goals (6–12 months)

**Focus:** Scale, social features, and advanced architecture.

### 🌟 User Profiles & Social Features
- Profiles with avatar, bio, and movie stats.
- Follow/friend system; see friends’ favorite movies.

### ☁️ Cloud Deployment & Database Scaling
- Deploy on AWS, Heroku, or DigitalOcean.
- Use PostgreSQL for better scalability.

### ⚡ Performance Optimizations
- Cache OMDb API responses for faster load.
- Minify CSS/JS, lazy-load images.

### 📱 Mobile App or PWA
- Turn MovieWeb into a Progressive Web App.
- Offline access to user’s movie list.

### 🔒 Security & Data Privacy
- HTTPS, password hashing, rate-limiting API calls.
- GDPR-compliant data handling.

---

### Optional Advanced Features
- 🎥 Movie Recommendations based on user ratings.
- 🏆 Leaderboards for top-rated movies/users.
- ✍️ Movie Reviews & Comments section per movie.
- 🔔 Email Notifications for updates, new features, or friend activity.


### ✨ Acknowledgments
Masterschool
- For the Codio project.
OMDb API
- for the free movies data API


## 🙋‍♂️ Author
**Abhisakh Sarma**
GitHub: [https://github.com/abhisakh](https://github.com/abhisakh)
_Contributions and feedback are always welcome!_
