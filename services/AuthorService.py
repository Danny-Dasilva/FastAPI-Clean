from typing import List, Optional

from fastapi import Depends
from repositories.AuthorRepository import AuthorRepository
from schemas.pydantic.AuthorSchema import Author
from schemas.pydantic.BookSchema import Book



class AuthorService:
    db: AuthorRepository

    def __init__(
        self, authorRepository: AuthorRepository = Depends()
    ) -> None:
        self.authorRepository = authorRepository

    def create(self, author: Author) -> Author:
        return self.db.create(
            **author
        )

    def delete(self, author_id: int) -> None:
        return self.db.delete(id=author_id
        )

    def get(self, author_id: int) -> Author:
        return self.db.get(id=author_id
        )

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Author]:
        return self.db.list()

    def update(
        self, author_id: int, author_body: Author
    ) -> Author:
        return self.db.update(
            author_id, Author(name=author_body.name)
        )

    def get_books(self, author_id: int) -> List[Book]:
        return self.db.get(id=author_id
        ).books
