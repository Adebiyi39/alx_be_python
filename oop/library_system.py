# Base Class
class Book:
    def _init_(self, title: str, author: str):
        self.title = title
        self.author = author

# Derived Class: EBook        
class EBook(Book):
    def _init_(self, title, author, file_size):
        super()._init_(title, author)
        self.file_size = file_size

# Derived Class: PrintBook
class PrintBook(Book):
    def _init_(self, title, author, page_count):
        super()._innit_(title, author)
        self.page_count = page_count

# Composition library 
class library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
            self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(
                    f"Title: {book.title}, Author: {book.author}, "
                    f"File Size: {book.file_size}KB"
                )
            elif isinstance(book, PrintBook):
                print(
                    f"Title: {book.title}, Author: {book.author}, "
                    f"Pages: {book.page_count}"
                )
            else:
                print(f"Title: {book.title}, Author: {book.author}")
