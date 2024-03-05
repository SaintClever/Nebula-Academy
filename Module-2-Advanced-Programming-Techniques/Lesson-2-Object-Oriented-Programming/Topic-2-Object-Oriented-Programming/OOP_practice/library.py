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
            print(f'Added "{book.title}" to Library:')
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

    def borrow_book(self, isbn, member):
        """Borrow Book"""
        print(member.borrowed_from())
        book_isbn = [book.isbn for book in self.books]

        if isbn not in book_isbn:
            print(f"ISBN: {isbn} not available")

        for book in self.books:
            if isbn == book.isbn and book.available_copies >= 1:
                book.available_copies -= 1
                print(
                    f'Borrowed "{book.title}"\nAvailable Copies: {book.available_copies}'
                )
            elif book.available_copies == 0:
                print(
                    f"Borrowed Book unsuccesful: {book.title}\nAvailable Copies: {book.available_copies}"
                )

    def return_book(self, isbn, member):
        """Return Book"""
        print(member.returned_from())
        for book in self.books:
            if isbn == book.isbn:
                book.available_copies += 1
                print(
                    f"Returning Book: {book.title}\nAvailable Copies: {book.available_copies}"
                )


class Member:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    def borrowed_from(self):
        return f"Book borrowed from: Name: {self.name} | Library ID: {self.library_id}"

    def returned_from(self):
        return f"Book returned from: {self.name} | Library ID: {self.library_id}"


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

book3 = Book(
    title="A Smarter Way to Learn Python: Learn it faster. Remember it longer.",
    author="Mark Myers",
    isbn="978-1974431472",
    available_copies=7,
)

print(
    f"Title: {book1.title}\nAuthor: {book1.author}\nISBN: {book1.isbn}\nAvailable Copies: {book1.available_copies}\n"
)

print(
    f"Title: {book2.title}\nAuthor: {book2.author}\nISBN: {book2.isbn}\nAvailable Copies: {book2.available_copies}\n"
)

library = Library()
library.add_book(book1)
print()

library.display_books()
print()

library.add_book(book2)
print()

library.display_books()
print()

library.add_book(book3)
print()

library.display_books()
print()

nesta = Member("Nesta", "903-5768")
saint_clever = Member("Saint. Clever", "867-5309")

library.borrow_book("978-0743273565", nesta)
print()

library.return_book("978-0743273565", nesta)
print()

library.borrow_book("978-1974431472", saint_clever)
print()

library.return_book("978-1974431472", saint_clever)
print()
