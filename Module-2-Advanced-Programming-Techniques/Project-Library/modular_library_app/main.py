from book import Book
from library import Library
from member import Member

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
