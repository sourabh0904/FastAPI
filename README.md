# FastAPI - MY API

A RESTful API built with FastAPI featuring CRUD operations, math utilities, API key authentication, and SQLModel database integration.

## Features

- Root and general greeting endpoints
- Math operations (add, update, delete) with API key protection
- Full CRUD for Items with SQLModel + SQLite/PostgreSQL
- Input validation using Pydantic
- CORS middleware enabled
- Interactive API docs (Swagger UI & ReDoc)
- Test suite with pytest

## Project Structure

```
FastAPI/
├── main.py              # App entry point, middleware & router setup
├── database.py          # Database engine & session management
├── models.py            # SQLModel table & request/response models
├── dependencies.py      # API key verification dependency
├── test_main.py         # Pytest test suite
├── requirement.txt      # Python dependencies
├── routes/
│   ├── root.py          # GET /
│   ├── general.py       # GET /general/about/{name}
│   ├── math.py          # POST /math/add, PUT /math/update, DELETE /math/delete
│   └── items.py         # CRUD endpoints for /items
└── venv/                # Virtual environment
```

## Prerequisites

- Python 3.9+
- pip

## Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/sourabh0904/FastAPI.git
   cd FastAPI
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS / Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirement.txt
   ```

4. **Set environment variables**

   Create a `.env` file in the project root:

   ```env
   DATABASE_URL=sqlite:///./test.db
   API_KEY=my-secret-key-12345
   ```

   - `DATABASE_URL` - Database connection string (defaults to SQLite if not set)
   - `API_KEY` - Secret key required for the `/math` endpoints

## Running the Server

```bash
uvicorn main:app --reload
```

The server starts at **http://127.0.0.1:8000**.

## API Documentation

Once the server is running, visit:

| Docs | URL |
|------|-----|
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

## API Endpoints

### Root

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Returns `{"Hello": "World"}` |

### General

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/general/about/{name}` | Returns a greeting for the given name (alphabetic only) |

### Math (requires `x-api-key` header)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/math/add` | Adds two positive integers |
| PUT | `/math/update` | Returns the two provided integers |
| DELETE | `/math/delete` | Returns a deletion confirmation message |

**Request body** for math endpoints:

```json
{
  "a": 5,
  "b": 10
}
```

### Items (CRUD)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/items` | Create a new item |
| GET | `/items` | List all items |
| GET | `/items/{item_id}` | Get an item by ID |
| PUT | `/items/{item_id}` | Update an item |
| DELETE | `/items/{item_id}` | Delete an item |

**Create/Update item body:**

```json
{
  "name": "Widget",
  "price": 9.99,
  "description": "Optional description"
}
```

## Running Tests

```bash
pytest test_main.py -v
```

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [SQLModel](https://sqlmodel.tiangolo.com/) - ORM (SQLAlchemy + Pydantic)
- [Uvicorn](https://www.uvicorn.org/) - ASGI server
- [Pytest](https://docs.pytest.org/) - Testing framework
