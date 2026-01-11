from collections.abc import Iterator, Iterable
from typing import List, Any

class Book:
    def __init__(self, title: str):
        self.title = title
    
    def __str__(self):
        return self.title

class BookCollection(Iterable):
    def __init__(self):
        self._books: List[Book] = []
    
    def add_book(self, book: Book):
        self._books.append(book)
    
    def __iter__(self) -> Iterator:
        return BookIterator(self._books)

class BookIterator(Iterator):
    def __init__(self, books: List[Book]):
        self._books = books
        self._index = 0
    
    def __next__(self) -> Book:
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        raise StopIteration()

if __name__ == "__main__":
    collection = BookCollection()
    collection.add_book(Book("Война и мир"))
    collection.add_book(Book("Преступление и наказание"))
    collection.add_book(Book("Мастер и Маргарита"))
    
    print("Книги в коллекции:")
    for book in collection:
        print(f"- {book}")
