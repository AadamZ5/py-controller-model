import pytest

from controllermodel import GenericController

@GenericController.register_model
class A:
    def __init__(self):
        self.a = "A variable"

    @GenericController.register_action(action="actiona")
    def myaction(self):
        print(self.a)
        return self.a

@GenericController.register_model
class B:
    def __init__(self):
        self.b = "B variable"

    @GenericController.register_action(action="actionb")
    def myaction(self):
        print(self.b)
        return self.b

def test_action():
    a = A()
    b = B()
    gc = GenericController()
    gc.connect_instance(a, b)
    assert gc.execute_action('actiona') == "A variable"
    assert gc.execute_action('actionb') == "B variable"