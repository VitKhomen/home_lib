from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.books import BookModel
from schemas.books import SAddBook, SBook


class BooksRepository:

    @classmethod
    async def get_books(
        cls,
        session: AsyncSession,
        limit: int = 10,
        offset: int = 0,
        keyword: str | None = None
    ) -> list[SBook]:
        query = select(BookModel)

        if keyword:
            query = query.where(BookModel.title.ilike(f"%{keyword}%"))

        result = await session.execute(query.limit(limit).offset(offset))
        books = result.scalars().all()

        return [SBook.model_validate(book) for book in books]

    @classmethod
    async def get_book(cls, session: AsyncSession, book_id: int) -> SBook | None:
        result = await session.execute(select(BookModel).where(BookModel.id == book_id))
        book = result.scalar_one_or_none()

        if book is None:
            return None

        return SBook.model_validate(book)

    @classmethod
    async def add_book(cls, session: AsyncSession, book: SAddBook) -> SBook:
        new_book = BookModel(
            title=book.title,
            author=book.author,
            published_year=book.published_year,
            pages=book.pages,
            is_read=book.is_read
        )
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)

        return SBook.model_validate(new_book)

    @classmethod
    async def update_book(cls, session: AsyncSession, book_id: int, book_data: SAddBook) -> SBook | None:
        result = await session.execute(select(BookModel).where(BookModel.id == book_id))
        book = result.scalar_one_or_none()

        if book is None:
            return None

        book.title = book_data.title
        book.author = book_data.author
        book.published_year = book_data.published_year
        book.pages = book_data.pages
        book.is_read = book_data.is_read

        await session.commit()
        await session.refresh(book)

        return SBook.model_validate(book)

    @classmethod
    async def delete_book(cls, session: AsyncSession, book_id: int) -> bool:
        result = await session.execute(select(BookModel).where(BookModel.id == book_id))
        book = result.scalar_one_or_none()

        if book is None:
            return False

        await session.delete(book)
        await session.commit()
        return True
