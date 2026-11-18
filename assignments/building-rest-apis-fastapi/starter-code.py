from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class BookInput(BaseModel):
    title: str
    author: str


class Book(BookInput):
    id: int


books = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien"),
    Book(id=2, title="A Wizard of Earthsea", author="Ursula K. Le Guin"),
]
next_book_id = 3

# TODO: Add GET routes to list books and retrieve one book by ID.
# TODO: Add a POST route to create a book.
# TODO: Add a PUT route to replace an existing book.
# TODO: Add a DELETE route to remove a book.
