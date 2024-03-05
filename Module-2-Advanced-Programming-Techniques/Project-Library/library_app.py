import pprint


class Book:
    def __init__(self, title, author, isbn, available_copies: int = 1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def display_info(self):
        return f"{self.title}\n{self.author}\n{self.isbn}"


class Library:
    def __init__(
        self, name, number: str | None = None, address: str | None = None
    ):  # If you set list = [] here all libraries will share the same books
        self.name = print(f"\n===== Welcome to {name.title()} =====\n")
        self.number = print(f"{name.title()} Number: {number}")
        self.addres = print(f"{name.title()} Address: {address}")
        self.books: list = []  # All libraries have different books

    def add_book(self, book):
        """Add Book"""
        # Add new book
        if book not in self.books:
            if book.available_copies > 0:
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
            else:
                print(
                    f"No available copies for {book.author}'s {book.title}: {book.available_copies}"
                )
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

book4 = Book(
    title="Candide",
    author="Voltaire",
    isbn="978-0486266893",
    available_copies=2,
)

print(
    f"Title: {book1.title}\nAuthor: {book1.author}\nISBN: {book1.isbn}\nAvailable Copies: {book1.available_copies}\n"
)

print(
    f"Title: {book2.title}\nAuthor: {book2.author}\nISBN: {book2.isbn}\nAvailable Copies: {book2.available_copies}\n"
)

manhattan_library = Library("Manhattan Library")
manhattan_library.add_book(book1)
manhattan_library.add_book(book2)
manhattan_library.name
print()

manhattan_library.display_books()
print()

queens_library = Library("Queens Library", "718-555-8888")
queens_library.add_book(book3)
queens_library.add_book(book3)
queens_library.add_book(book4)
queens_library.name
queens_library.number
print()

queens_library.display_books()
print()

queens_library.add_book(book2)
print()

queens_library.display_books()
print()

queens_library.add_book(book3)
print()

queens_library.display_books()
print()

nesta = Member("Nesta", "903-5768")
saint_clever = Member("Saint. Clever", "867-5309")

queens_library.borrow_book("978-0743273565", nesta)
print()

queens_library.return_book("978-0743273565", nesta)
print()

queens_library.borrow_book("978-1974431472", saint_clever)
print()

queens_library.return_book("978-1974431472", saint_clever)
print()

queens_library.display_books()
print()

queens_library.add_book(book4)
print()

queens_library.display_books()
print()
