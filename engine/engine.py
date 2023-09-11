from abc import ABC, abstractmethod
from car import Car

class Engine(Car):
    
    @abstractmethod
    def needs_service(self):
        pass

    