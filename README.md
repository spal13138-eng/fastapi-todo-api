
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)

# FastAPI Todo API with JWT Authentication

A secure multi-user Todo API built using FastAPI. This project allows users to register, log in, and manage their own todos with JWT-based authentication and authorization.

Each user can only access their own tasks, making the API secure and suitable for real-world backend learning.

---

## Features

* User registration
* Secure password hashing
* JWT authentication
* User login system
* Protected routes
* Create, Read, Update, Delete todos
* User-specific todo access
* Authorization checks
* PostgreSQL database integration
* SQLAlchemy ORM
* Alembic migrations
* Environment variable support using `.env`

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic
* JWT Authentication
* Passlib / bcrypt
* Pydantic
* Uvicorn

---

## Project Structure

```text
app/
│── main.py
│── models.py
│── schemas.py
│── database.py
│── oauth2.py
│── utils.py
│── config.py
│── routers/
│   ├── auth.py
│   ├── user.py
│   └── todo.py
│
├── migrations/
├── .env.example
├── requirements.txt
├── alembic.ini
├── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <https://github.com/spal13138-eng/fastapi-todo-api.git>
cd <Todo API>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

For Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

Create a `.env` file in the root directory and add the following:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Example PostgreSQL URL:

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost/Todo
```

---

## Database Migration

Run Alembic migrations:

```bash
alembic upgrade head
```

Whenever you change your models:

```bash
alembic revision --autogenerate -m "your message"
alembic upgrade head
```

---

## Run the Server

```bash
uvicorn app.main:app --reload
```

Server will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Authentication Routes

| Method | Endpoint | Description                     |
| ------ | -------- | ------------------------------- |
| POST   |`/register` | Register a new user             |
| POST   | `/login` | Login user and get access token |

### Todo Routes

| Method | Endpoint      | Description                     |
| ------ | ------------- | ------------------------------- |
| GET    | `/todos`      | Get all todos of logged-in user |
| POST   | `/todos`      | Create a new todo               |
| GET    | `/todos/{id}` | Get a single todo               |
| PUT    | `/todos/{id}` | Update a todo                   |
| DELETE | `/todos/{id}` | Delete a todo                   |

---

## Authentication Flow

1. Register a new user
2. Login using email and password
3. Receive JWT token
4. Send token in Authorization header
5. Access protected routes

Example:

```text
Authorization: Bearer your_jwt_token
```

---

## Example Todo Response

```json
{
  "id": 1,
  "title": "Complete FastAPI project",
  "description": "Add JWT auth and Alembic",
  "completed": false,
  "owner_id": 1
}
```

---

## Example Login Response

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

---

## Future Improvements

* Add due dates
* Add task priority
* Add pagination
* Add search and filtering
* Add Docker support
* Add deployment
* Add frontend integration

---

## Author

Shiva
