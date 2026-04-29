from fastapi import APIRouter, HTTPException, status

from database import SessionDep
from schemas.books import SAddBook, SBook
from repository.books import BooksRepository


router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/")
async def get_books(
    session: SessionDep,
    limit: int = 10,
    offset: int = 0,
    keyword: str | None = None
) -> list[SBook]:
    return await BooksRepository.get_books(session, limit, offset, keyword)


@router.get("/{book_id}")
async def get_book(session: SessionDep, book_id: int) -> SBook:
    result = await BooksRepository.get_book(session, book_id)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_book(session: SessionDep, book: SAddBook) -> SBook:
    return await BooksRepository.add_book(session, book)


@router.put("/{book_id}")
async def update_book(session: SessionDep, book_id: int, book_data: SAddBook) -> SBook:
    result = await BooksRepository.update_book(session, book_id, book_data)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )

    return result


@router.delete("/{book_id}", status_code=204)
async def delete_book(session: SessionDep, book_id: int):
    success = await BooksRepository.delete_book(session, book_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )
