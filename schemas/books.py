from pydantic import BaseModel, Field, ConfigDict


class SAddBook(BaseModel):
    title: str = Field(
        ..., min_length=1,
        max_length=200,
        title="Title of the book",
    )
    author: str = Field(
        ..., min_length=1,
        max_length=100,
        title="Author of the book",
    )
    published_year: int = Field(
        ..., ge=0,
        title="Publication year of the book",
    )
    pages: int = Field(
        ..., ge=1,
        title="Number of pages in the book",
    )
    is_read: bool = Field(
        default=False,
        title="Has the book been read?",
        description="Set to `true` if the book has been read, otherwise `false`"
    )


class SBook(SAddBook):
    id: int

    model_config = ConfigDict(from_attributes=True)
