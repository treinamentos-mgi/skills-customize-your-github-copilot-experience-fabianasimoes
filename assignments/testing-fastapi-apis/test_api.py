import pytest
from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_api_data():
    main.reset_books()


def test_list_books_returns_initial_books():
    response = client.get("/books")

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["title"] == "The Hobbit"


# TODO: Add tests for retrieving, creating, and updating books.
# TODO: Add tests for invalid input, missing books, and deleting a book.
