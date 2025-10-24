# Friendly Teaching Style: sqlalchemy_orm_explained_friendly.md

# Understanding SQLAlchemy ORM through Real Examples

## Introduction
This guide is for Python developers familiar with SQL but new to ORMs.
We’ll explore how SQLAlchemy maps Python classes to tables, and how `db.relationship()` works using real examples.

---

## Example Tables

### User Table
| id | name   |
|----|--------|
| 1  | Alice  |
| 2  | Bob    |

### Movie Table
| id | name           | year | user_id |
|----|----------------|------|---------|
| 1  | Inception      | 2010 | 1       |
| 2  | Interstellar   | 2014 | 1       |
| 3  | The Dark Knight| 2008 | 2       |

---

## SQLAlchemy Models
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    movies = db.relationship('Movie', backref='user', lazy=True)

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```

---

## Without `db.relationship()`

### Get all movies for Alice

#### SQL
```sql
SELECT * FROM movie
JOIN user ON movie.user_id = user.id
WHERE user.name = 'Alice';
```

#### Python
```python
alice = User.query.filter_by(name='Alice').first()
movies = Movie.query.filter_by(user_id=alice.id).all()
for movie in movies:
    print(movie.name)
```

**Output:**
```
Inception
Interstellar
```

**Disadvantages:**
- Must manually filter/join
- Work with IDs, not objects
- Verbose and repetitive code

---

## With `db.relationship()`

### Access movies directly

```python
alice = User.query.filter_by(name='Alice').first()
for movie in alice.movies:
    print(movie.name)
```

SQLAlchemy internally executes:
```sql
SELECT * FROM movie WHERE movie.user_id = 1;
```

**Output:**
```
Inception
Interstellar
```

### Access user from movie

```python
movie = Movie.query.filter_by(name='The Dark Knight').first()
print(movie.user.name)
```
SQL internally:
```sql
SELECT * FROM user WHERE id = 2;
```
**Output:**
```
Bob
```

---

## Visual Diagram
```
┌───────────────┐          ┌──────────────────────────────┐
│    USER TABLE │          │         MOVIE TABLE          │
│---------------│          │------------------------------│
│ id | name     │◄────────┤ user_id | name               │
│----|----------│          │------------------------------│
│ 1  | Alice    │          │ 1 | Inception               │
│ 2  | Bob      │          │ 2 | Interstellar            │
└───────────────┘          └──────────────────────────────┘

user.movies  → [Movie("Inception"), Movie("Interstellar")]
movie.user   → User("Alice")
```

---

## Key Takeaways
- Foreign keys connect tables at the database level
- `db.relationship()` connects Python objects
- With it, you navigate objects directly, ORM executes SQL for you
- Without it, you must write joins manually

---
# Formal Documentation Style: sqlalchemy_orm_basics_reference.md

# SQLAlchemy ORM Basics Reference

## Overview
This document provides a reference for SQLAlchemy ORM usage in Python applications. It covers model definitions, foreign keys, relationships, and SQL equivalences.

## Models

### User Model
```python
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, doc='Primary key of the user')
    name = db.Column(db.String(100), nullable=False, doc='Name of the user')
    movies = db.relationship('Movie', backref='user', lazy=True, doc='One-to-many relationship to Movie')
```

### Movie Model
```python
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True, doc='Primary key of the movie')
    name = db.Column(db.String(100), nullable=False, doc='Name of the movie')
    year = db.Column(db.Integer, nullable=False, doc='Release year')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, doc='Foreign key linking to User')
```

## Foreign Key
- `user_id` in `Movie` references `User.id`
- Ensures referential integrity at the database level

## Relationship
- `movies = db.relationship('Movie', backref='user', lazy=True)`
- Establishes a bidirectional Python-level association
- Allows `user.movies` and `movie.user` access

## SQL Equivalence
| ORM Access           | SQL Equivalent |
|----------------------|----------------|
| user.movies          | SELECT * FROM movie WHERE user_id = user.id |
| movie.user           | SELECT * FROM user WHERE id = movie.user_id |

## Example Queries
```python
# Get movies by user
alice = User.query.get(1)
for movie in alice.movies:
    print(movie.name)

# Get user from movie
movie = Movie.query.get(3)
print(movie.user.name)
```

## Advantages
- Cleaner, Pythonic object navigation
- Automatic SQL generation for joins
- Reduces repetitive filtering code

## Best Practices
- Follow PEP 8 naming conventions
- Use `lazy=True` or `joined` loading based on query patterns
- Always define `backref` for bidirectional access
- Use descriptive docstrings for clarity

## Visual Diagram
```
┌───────────────┐          ┌──────────────────────────────┐
│    USER TABLE │          │         MOVIE TABLE          │
│ id | name     │◄─────────┤ user_id | name               │
└───────────────┘          └──────────────────────────────┘
user.movies  → list of Movie objects
movie.user   → single User object
```

---
Both documents include **real table data**, **code block comparisons**, and **diagrams** to illustrate ORM concepts versus raw SQL joins.

# SQLAlchemy Session Manual

## Overview
The `Session` object in SQLAlchemy manages all interactions between Python objects and the database. It tracks objects, handles commits, rollbacks, and maintains the connection.

In Flask-SQLAlchemy, `db.session` is a preconfigured session instance.

---

## 1️⃣ add(instance)
**Purpose:** Add a single object to the session (pending insertion).

```python
alice = User(name="Alice")
db.session.add(alice)
db.session.commit()
```

---

## 2️⃣ add_all([instances])
**Purpose:** Add multiple objects at once.

```python
bob = User(name="Bob")
carol = User(name="Carol")
db.session.add_all([bob, carol])
db.session.commit()
```

---

## 3️⃣ commit()
**Purpose:** Persist all pending changes to the database.

```python
new_movie = Movie(name="Inception", year=2010, user_id=1)
db.session.add(new_movie)
db.session.commit()
```

---

## 4️⃣ rollback()
**Purpose:** Undo all uncommitted changes.

```python
try:
    new_movie = Movie(name="ErrorMovie", year=2022, user_id=999)
    db.session.add(new_movie)
    db.session.commit()
except:
    db.session.rollback()
```

---

## 5️⃣ delete(instance)
**Purpose:** Mark an object for deletion.

```python
movie = Movie.query.get(1)
db.session.delete(movie)
db.session.commit()
```

---

## 6️⃣ query()
**Purpose:** Start ORM queries.

```python
users = db.session.query(User).all()
movies = db.session.query(Movie).filter_by(user_id=1).all()
```

---

## 7️⃣ flush()
**Purpose:** Push changes to the DB without committing.

```python
new_user = User(name="Dave")
db.session.add(new_user)
db.session.flush()
print(new_user.id)
db.session.commit()
```

---

## 8️⃣ expire(instance) / expire_all()
**Purpose:** Mark object attributes as expired for reload on next access.

```python
alice = User.query.get(1)
db.session.expire(alice)
print(alice.name)
```

---

## 9️⃣ refresh(instance)
**Purpose:** Reload the object immediately from the database.

```python
bob = User.query.get(2)
db.session.refresh(bob)
print(bob.name)
```

---

## 10️⃣ close()
**Purpose:** Close the session and release the connection.

```python
db.session.close()
```

---

## 11️⃣ remove() (Flask-SQLAlchemy specific)
**Purpose:** Remove the session from thread-local storage.

```python
db.session.remove()
```

---

## 12️⃣ merge(instance)
**Purpose:** Re-associate a detached object with the session.

```python
alice_detached = User(id=1, name="Alice Updated")
db.session.merge(alice_detached)
db.session.commit()
```

---

## 13️⃣ bulk_save_objects(objects)
**Purpose:** Efficiently insert/update many objects at once.

```python
movies = [
    Movie(name="Tenet", year=2020, user_id=1),
    Movie(name="Memento", year=2000, user_id=1)
]
db.session.bulk_save_objects(movies)
db.session.commit()
```

---

## Object Lifecycle & Session Diagram

```
             +------------+
Transient    |   Python   |  (Created but not added to session)
   obj      +------------+
        db.session.add(obj)
                 |
                 v
             +------------+
Pending      |  Session   |  (Tracked by session, waiting for commit)
   obj      +------------+
        db.session.commit()
                 |
                 v
             +------------+
Persistent   |  Database  |  (Now saved in DB)
   obj      +------------+
        db.session.delete(obj)
                 |
                 v
             +------------+
Deleted     |  Session   |  (Marked for deletion; removed on commit)
   obj      +------------+
```

- **Transient:** New Python object, not tracked.
- **Pending:** Added to session with `.add()`, not yet committed.
- **Persistent:** Saved in the database after `.commit()`.
- **Deleted:** Marked for deletion via `.delete()`, removed on commit.

---

## Summary Table

| Method | Purpose |
|--------|---------|
| `add(instance)` | Add a single object |
| `add_all([instances])` | Add multiple objects |
| `commit()` | Save all pending changes |
| `rollback()` | Undo pending changes |
| `delete(instance)` | Mark object for deletion |
| `query()` | Start queries |
| `flush()` | Push changes without commit |
| `expire()` / `expire_all()` | Expire object(s) to reload later |
| `refresh(instance)` | Reload object immediately from DB |
| `close()` | Close session connection |
| `remove()` | Remove session (Flask-SQLAlchemy) |
| `merge(instance)` | Re-associate detached object |
| `bulk_save_objects()` | Bulk insert/update objects |

