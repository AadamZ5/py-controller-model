from abc import ABC, abstractmethod
from typing import Optional, Union, List, Tuple

class ControllerInterface(ABC):

    @classmethod
    @abstractmethod
    def register_model(cls, register_cls):
        pass

    @classmethod
    @abstractmethod
    def register_action(self):
        pass

    @abstractmethod
    def connect_instance(self, instance_of_class: Union[List[object], Tuple[object], object], *additional_instances: Tuple[object]):
        pass
