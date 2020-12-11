from abc import ABC, abstractmethod
from typing import Optional, Union, List, Tuple

class ControllerInterface(ABC):

    @classmethod
    @abstractmethod
    def register_model(cls, register_cls):
        """
        Register a model as connectable.
        """
        pass

    @classmethod
    @abstractmethod
    def register_action(self):
        """
        Registers a potential action from a model.
        """
        pass

    @abstractmethod
    def connect_instance(self, instance_of_class: Union[List[object], Tuple[object], object], *additional_instances: Tuple[object]):
        """
        Connect instances of the model(s) to this controller.
        """
        pass
