class Member:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    def borrowed_from(self):
        return f"Book borrowed from: Name: {self.name} | Library ID: {self.library_id}"

    def returned_from(self):
        return f"Book returned from: {self.name} | Library ID: {self.library_id}"
