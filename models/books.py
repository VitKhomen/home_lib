from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str]
    author: Mapped[str]
    published_year: Mapped[int] = mapped_column(nullable=True, default=None)
    pages: Mapped[int] = mapped_column(nullable=True, default=None)
    is_read: Mapped[bool] = mapped_column(insert_default=False, default=False)
