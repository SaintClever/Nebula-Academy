class Book:
    def __init__(self, title, author, isbn, available_copies: int = 1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def display_info(self):
        return f"{self.title}\n{self.author}\n{self.isbn}"
