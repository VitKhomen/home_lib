import uvicorn

from fastapi import FastAPI
from contextlib import asynccontextmanager

from routers.books import router as books_router
from database import engine, Base
from models.books import BookModel


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Database is ready")

    yield

    print("Shutting down server")

app = FastAPI(
    lifespan=lifespan,
    title="Home Library API",
    description="A simple API for managing your home library",
    version="1.0.0"
)

app.include_router(books_router)

if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
