from abc import ABC, abstractmethod

class IDatabaseBRM(ABC):
    # возвращает tuple(), содержащий:
    # 1. массив со всеми книгами (объекты book);
    # 2. количество книг каждого типа (count).
    @abstractmethod
    def getBookCovers(self):
        """Get book covers"""
        
class IDatabaseGUI(ABC):
    # добавляет в базу данных информацию о новой книге.
    @abstractmethod
    def addBook(self, book, count):
        """Add book"""
    
    # возвращает tuple(), содержащий:
    # 1. массив со всеми книгами (объекты book);
    # 2. количество книг каждого типа (count).
    @abstractmethod
    def getAllBooks(self):
        """Get all books"""
    
    # на вход получает id распознанной книги и процент скидки,
    # изменяет текущую скидку для книги с полученным id.
    @abstractmethod
    def addDiscount(self, book_id, new_discount):
        """Add discount"""
    
    # на вход получает id распознанной книги и количество книг,
    # изменяет количество книг на addition.
    @abstractmethod
    def replenishBooks(self, book_id, addition):
        """Replenish books"""