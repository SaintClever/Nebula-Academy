import pprint


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