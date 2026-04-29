# Home Library API

A simple and efficient REST API for managing your personal book collection, built with FastAPI and SQLAlchemy.

## Features

- ✨ Full CRUD operations for books
- 🔍 Search books by title
- 📄 Pagination support
- 🚀 Async/await for better performance
- 📊 PostgreSQL database with SQLAlchemy ORM
- 🎯 Clean architecture with repository pattern
- 📝 Automatic API documentation (Swagger/OpenAPI)

## Tech Stack

- **Framework**: FastAPI 0.136.1
- **Database**: PostgreSQL (via asyncpg)
- **ORM**: SQLAlchemy 2.0.49 (async)
- **Validation**: Pydantic 2.13.3
- **Server**: Uvicorn 0.46.0

## Prerequisites

- Python 3.10+
- PostgreSQL database

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd home-library-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:
```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/library_db
```

Replace `username`, `password`, and `library_db` with your PostgreSQL credentials.

## Running the Application

Start the development server:
```bash
python main.py
```

Or use uvicorn directly:
```bash
uvicorn main:app --reload --host localhost --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Books

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/` | Get all books (with pagination and search) |
| GET | `/books/{book_id}` | Get a specific book by ID |
| POST | `/books/` | Add a new book |
| PUT | `/books/{book_id}` | Update an existing book |
| DELETE | `/books/{book_id}` | Delete a book |

### Query Parameters

**GET `/books/`**
- `limit` (int, default: 10) - Number of books to return
- `offset` (int, default: 0) - Number of books to skip
- `keyword` (str, optional) - Search books by title

### Request/Response Examples

#### Get all books
```bash
curl http://localhost:8000/books/
```

#### Search books
```bash
curl "http://localhost:8000/books/?keyword=python&limit=5"
```

#### Add a new book
```bash
curl -X POST http://localhost:8000/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "published_year": 2008,
    "pages": 464,
    "is_read": true
  }'
```

#### Update a book
```bash
curl -X PUT http://localhost:8000/books/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "published_year": 2008,
    "pages": 464,
    "is_read": true
  }'
```

#### Delete a book
```bash
curl -X DELETE http://localhost:8000/books/1
```

## Book Schema

### SAddBook (Request body)
```json
{
  "title": "string (1-200 chars, required)",
  "author": "string (1-100 chars, required)",
  "published_year": "integer (≥0, required)",
  "pages": "integer (≥1, required)",
  "is_read": "boolean (default: false)"
}
```

### SBook (Response)
```json
{
  "id": "integer",
  "title": "string",
  "author": "string",
  "published_year": "integer",
  "pages": "integer",
  "is_read": "boolean"
}
```

## Project Structure

```
.
├── database.py          # Database configuration and session management
├── main.py             # Application entry point
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (create this)
├── models/
│   └── books.py       # SQLAlchemy models
├── schemas/
│   └── books.py       # Pydantic schemas
├── repository/
│   └── books.py       # Database operations
└── routers/
    └── books.py       # API endpoints
```

## Database Schema

### Books Table
| Column | Type | Constraints |
|--------|------|-------------|
| id | INTEGER | PRIMARY KEY, AUTO INCREMENT |
| title | VARCHAR | NOT NULL |
| author | VARCHAR | NOT NULL |
| published_year | INTEGER | NULLABLE |
| pages | INTEGER | NULLABLE |
| is_read | BOOLEAN | DEFAULT FALSE |

## Development

The application uses:
- **Repository Pattern**: Separation of data access logic
- **Dependency Injection**: FastAPI's dependency system for database sessions
- **Async Operations**: All database operations are asynchronous
- **Type Hints**: Full type annotation support

## Error Handling

The API returns appropriate HTTP status codes:
- `200 OK` - Successful GET/PUT requests
- `201 Created` - Successful POST requests
- `204 No Content` - Successful DELETE requests
- `404 Not Found` - Resource not found
- `422 Unprocessable Entity` - Validation errors

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or feedback, please open an issue on GitHub.