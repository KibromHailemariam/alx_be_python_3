# library_composition.py

# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Derived class 1
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


# Derived class 2
class PrintBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages


# Composition class
class Library:
    def __init__(self):
        self.books = []  # holds Book, EBook, or PrintBook objects

    def add_book(self, book):
        self.books.append(book)  # adds book to the list

    def list_books(self):
        for book in self.books:
            # check the book type to display extra details
            if isinstance(book, EBook):
                print(f"E-Book: {book.title} by {book.author} ({book.file_size}MB)")
            elif isinstance(book, PrintBook):
                print(f"Print Book: {book.title} by {book.author} ({book.pages} pages)")
            else:
                print(f"Book: {book.title} by {book.author}")


# Example usage
if __name__ == "__main__":
    library = Library()

    b1 = Book("Atomic Habits", "James Clear")
    b2 = EBook("Python 101", "John Doe", 10)
    b3 = PrintBook("Clean Code", "Robert C. Martin", 450)

    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)

    library.list_books()
