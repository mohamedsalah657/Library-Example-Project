from abc import ABC, abstractmethod

class IBook_Repository(ABC):
    @abstractmethod
    def get_book(self, id):
        pass

class ILibrary_Operation(ABC):
    @abstractmethod    
    def execute(self, book, user_id):
        pass
    
class BOOK_Repository(IBook_Repository):
    def get_book(self, id):
        return Book("Example Book", "Author Name", id)
    
class Borrow_books(ILibrary_Operation):
    def execute(self, book, user_id):
        print(f"Book {book.id} borrowed to {user_id}")
        
class Book:
    def __init__(self, title, author, id): 
        self.title = title
        self.author = author
        self.id = id
        
repo = BOOK_Repository()
Borrow_book_operation = Borrow_books()
book = repo.get_book("12345")
Borrow_book_operation.execute(book, "11")
