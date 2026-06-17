# Blog API with Authentication

A RESTful Blog API built using FastAPI, MySQL, and SQLAlchemy.

## Features

- User Registration
- User Login
- Password Hashing using bcrypt
- Create Blog
- Get All Blogs
- Get Single Blog
- Update Blog
- Delete Blog
- Swagger API Documentation

## Technologies Used

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Passlib
- Bcrypt
- Uvicorn

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd blog_api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m uvicorn main:app --reload
```

## API Endpoints

### Authentication

- POST /register
- POST /login

### Blogs

- POST /blogs
- GET /blogs
- GET /blogs/{id}
- PUT /blogs/{id}
- DELETE /blogs/{id}

## API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

## Author

Achal Jogi
