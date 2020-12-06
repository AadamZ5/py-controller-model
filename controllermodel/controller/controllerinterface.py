from abc import ABC, abstractmethod

class ControllerInterface(ABC):
    
    @classmethod
    @abstractmethod
    def register_model(cls, register_cls):
        pass

    @abstractmethod
    def register_action(self):
        pass
