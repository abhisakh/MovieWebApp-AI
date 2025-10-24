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
│ id | name     │◄────────┤ user_id | name               │
└───────────────┘          └──────────────────────────────┘
user.movies  → list of Movie objects
movie.user   → single User object
```

---
Both documents include **real table data**, **code block comparisons**, and **diagrams** to illustrate ORM concepts versus raw SQL joins.

