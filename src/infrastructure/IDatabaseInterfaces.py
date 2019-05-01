from abc import ABC, abstractmethod

class IDatabaseRM(ABC):
    # возвращает массив объектов exhibit.
    @abstractmethod
    def getExhibitImages(self):
        """Get exhibit images"""
        
class IDatabaseGUI(ABC):
    # добавляет в базу данных информацию о новом экспонате.
    @abstractmethod
    def addExhibit(self, exhibit):
        """Add exhibit"""
    
    # возвращает массив объектов exhibit.
    @abstractmethod
    def getAllExhibits(self):
        """Get all exhibits"""
    
    # на вход получает id распознанного экспоната,
    # возвращает объект exhibit.
    @abstractmethod
    def getExhibit(self, ex_id):
        """Get exhibit"""
