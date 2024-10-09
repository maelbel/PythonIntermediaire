from abc import ABC, abstractmethod

class IDBManager(ABC):
    
    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def select(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass