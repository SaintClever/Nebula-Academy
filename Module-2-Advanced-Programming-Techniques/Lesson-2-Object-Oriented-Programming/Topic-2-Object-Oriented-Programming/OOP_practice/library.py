import pprint


class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def display_info(self):
        return f"{self.title}\n{self.author}\n{self.isbn}"


class Library:
    def __init__(self, books: list = []):
        self.books = books

    def add_book(self, book):
        """Add Book"""
        # Add new book
        if book not in self.books:
            self.books.append(book)
            books = [
                {
                    "title": book.title,
                    "author": book.author,
                    "isbn": book.isbn,
                    "available_copies": book.available_copies,
                }
                for book in self.books
            ]
            print(f"{book.title} added to Library: ")
            pprint.pprint(books)
        # Add additional copy if book already exist
        else:
            book.available_copies += 1
            print(
                f"Additional copy available for {book.title}: copies {book.available_copies}"
            )

        return self.books

    def display_books(self):
        """Display Books"""
        books = [
            {
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "available_copies": book.available_copies,
            }
            for book in self.books
        ]
        print(f"Display current books available: ")
        pprint.pprint(books)
        return self.books

    def borrow_book(self, isbn):
        # TODO: If there is one available book remove it from list else if there are multiple available books remove one available copy
        isbns_available_copies = [
            {"isbn": book.isbn, "available_copies": book.available_copies}
            for book in self.books
        ]

        print(isbns_available_copies)

        for i in isbns_available_copies:
            print(i, isbn)
            # TODO: if isbn exist and availabiliy is greater 1 or greater you can borrow
            print(isbn == i.get("isbn"), i.get("available_copies") >= 1)
            # TODO: else isbn doesn't exist
            # TODO: else there are no available copies to borrow

        isbn_numbers = [book.isbn for book in self.books]

        if isbn in isbn_numbers:
            borrowed_book = self.books.pop(isbn_numbers.index(isbn))
            book_titles = [book.title for book in self.books]
            print(f"Borrowed Book: {borrowed_book.title}\nCurrent Books: {book_titles}")
            return borrowed_book
        else:
            print(f"Borrow book current request not available for: {isbn}")

    def return_book(self, isbn):
        borrowed_book = self.borrow_book(self, isbn)
        if isbn in borrowed_book:
            self.books.append(borrowed_book.pop(isbn))


book1 = Book(
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    isbn="978-0743273565",
    available_copies=5,
)

book2 = Book(
    title="To Kill a Mockingbird",
    author="Harper Lee",
    isbn="978-0061120084",
    available_copies=3,
)

print(
    f"Title: {book1.title}\nAuthor: {book1.author}\nISBN: {book1.isbn}\nAvailable Copies: {book1.available_copies}"
)
print()

print(
    f"Title: {book2.title}\nAuthor: {book2.author}\nISBN: {book2.isbn}\nAvailable Copies: {book2.available_copies}"
)
print()

library = Library()
library.add_book(book1)
print()
library.display_books()
print()

library.add_book(book2)
print()
library.display_books()
print()

library.add_book(book2)
print()
library.display_books()
print()

library.borrow_book("978-0743273565")
print()
library.display_books()
print()
