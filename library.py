# library.py

class Book:
    def __init__(self, title, author, book_id, total_copies):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.total_copies = total_copies
        self.available_copies = total_copies


class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_records = []

    def add_book(self, book):
        if book.book_id in self.books:
            return "Book with this ID already exists."
        self.books[book.book_id] = book
        return "Book added successfully."

    def search_by_title(self, title):
        return [b for b in self.books.values() if title.lower() in b.title.lower()]

    def search_by_author(self, author):
        return [b for b in self.books.values() if author.lower() in b.author.lower()]

    def borrow_book(self, book_id, user_name):
        if book_id not in self.books:
            return "Book ID not found."
        book = self.books[book_id]
        if book.available_copies <= 0:
            return "No copies available."
        book.available_copies -= 1
        self.borrowed_records.append((user_name, book.title))
        return f"{user_name} borrowed '{book.title}'."

    def return_book(self, book_id, user_name):
        if book_id not in self.books:
            return "Book ID not found."
        self.books[book_id].available_copies += 1
        return f"{user_name} returned the book."
