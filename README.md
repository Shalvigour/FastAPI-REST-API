# ⚡ FastAPI REST API — Blog API with JWT Authentication

> A production-style RESTful API built with Python and FastAPI, featuring JWT-based authentication, SQLAlchemy ORM, Pydantic validation, and auto-generated interactive documentation.

---

## 📌 Overview

A clean, modular Blog REST API that demonstrates core backend engineering principles — authentication, database integration, request validation, and proper HTTP semantics — all built with FastAPI's async-first Python framework.

---

## ✨ Features

- 🔐 **JWT Authentication** — Token-based auth using `python-jose`, secrets loaded via `.env`
- 📝 **Full CRUD for Blogs** — Create, Read (all + single), Update, Delete
- 🔒 **Protected Routes** — Create endpoint requires a valid Bearer token
- 🗄️ **SQLAlchemy ORM** — Database-agnostic, works with SQLite locally and PostgreSQL in production
- ✅ **Pydantic Schemas** — Request/response validation with automatic serialization
- 📖 **Auto-generated Docs** — Swagger UI at `/docs` and ReDoc at `/redoc` out of the box
- 🌱 **Environment Variables** — Sensitive config loaded via `python-dotenv`

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.10+** | Core language |
| **FastAPI** | Web framework |
| **SQLAlchemy** | ORM & database layer |
| **Pydantic** | Data validation & serialization |
| **python-jose** | JWT token creation & verification |
| **python-dotenv** | Environment variable management |
| **Uvicorn** | ASGI server |

---

## 📁 Project Structure

```
FastAPI-REST-API/
│
├── main.py          # App entry point — all route definitions
├── auth.py          # JWT token creation & verification logic
├── database.py      # SQLAlchemy engine, session, and DB setup
├── models.py        # SQLAlchemy ORM models (Blog table)
├── schemas.py       # Pydantic schemas for request/response validation
├── .env             # Environment variables (NOT committed — see setup)
├── .gitignore
└── README.md
```

---

## 🔌 API Endpoints

### Auth
| Method | Endpoint | Auth Required | Description |
|--------|---------|:---:|-------------|
| `POST` | `/login` | ❌ | Returns a JWT access token |

### Blogs
| Method | Endpoint | Auth Required | Description |
|--------|---------|:---:|-------------|
| `GET` | `/blogs` | ❌ | Fetch all blog posts |
| `GET` | `/blogs/{id}` | ❌ | Fetch a single blog post by ID |
| `POST` | `/blogs` | ✅ | Create a new blog post |
| `PUT` | `/blogs/{id}` | ❌ | Update an existing blog post |
| `DELETE` | `/blogs/{id}` | ❌ | Delete a blog post |

> Protected routes require `Authorization: Bearer <token>` in the request header.

---

## ⚙️ Setup & Run

### Prerequisites
- Python 3.10+
- pip

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/Shalvigour/FastAPI-REST-API.git
cd FastAPI-REST-API
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install fastapi uvicorn sqlalchemy python-jose[cryptography] python-dotenv pydantic
```

**4. Create your `.env` file**

Create a `.env` file in the root folder (this is gitignored — never commit it):
```
SECRET_KEY=your_strong_random_secret_key_here
```

Generate a strong secret key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**5. Run the server**
```bash
uvicorn main:app --reload
```

Server runs at `http://localhost:8000`

---

## 📖 Interactive API Docs

Once the server is running, FastAPI auto-generates:

| Interface | URL |
|-----------|-----|
| **Swagger UI** | `http://localhost:8000/docs` |
| **ReDoc** | `http://localhost:8000/redoc` |

Use Swagger UI to test all endpoints directly in the browser — no Postman needed.

---

## 🧪 Testing the API

**Step 1 — Get a token**
```bash
curl -X POST http://localhost:8000/login
```

**Step 2 — Create a blog (use the token)**
```bash
curl -X POST http://localhost:8000/blogs \
  -H "Authorization: Bearer <your_token>" \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Blog", "content": "Hello World!"}'
```

**Step 3 — Read all blogs**
```bash
curl http://localhost:8000/blogs
```

---

## 🔐 Security Notes

> ⚠️ The following are **never committed** to this repository:

| Sensitive Item | How to Handle |
|---------------|--------------|
| `.env` file | Create locally with your own `SECRET_KEY` |
| `SECRET_KEY` | Use a cryptographically strong random string |

The `SECRET_KEY` is loaded via `os.environ.get("SECRET_KEY")` — never hardcoded.

---

## 🚫 What's Not Included

| Excluded Item | Reason |
|--------------|--------|
| `.env` | Contains sensitive JWT secret |
| `__pycache__/` | Python bytecode — auto-generated, should be gitignored |
| `*.db` | Local SQLite database file |

> 💡 **Note:** The `__pycache__/` folder is currently present in the repo. Add `__pycache__/` to `.gitignore` and run `git rm -r --cached __pycache__/` to remove it.

---

## 🎯 Key Concepts Demonstrated

- REST API design with proper HTTP methods and status codes
- Stateless JWT authentication with expiry
- SQLAlchemy ORM with dependency injection (`Depends`)
- Pydantic schemas separating input validation from DB models
- Environment-based secret management with `python-dotenv`
- FastAPI's automatic OpenAPI documentation generation

---

## 👩‍💻 Author

**Shalvi Gaur** — [GitHub](https://github.com/Shalvigour) · [LinkedIn](https://linkedin.com/in/shalvi-gour)
