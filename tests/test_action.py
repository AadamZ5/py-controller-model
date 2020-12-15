import pytest

from controllermodel import GenericController

@GenericController.register_model
class A:
    def __init__(self):
        self.a = "A variable"

    @GenericController.register_action(action="action")
    def myaction(self):
        print(self.a)
        return self.a

    @GenericController.register_action
    def myaction_copy(self):
        print(self.a)
        return self.a

def test_action():
    a = A()
    gc = GenericController(a)
    assert gc.execute_action('action') == "A variable"

def test_action_unnamed():
    a = A()
    gc = GenericController(a)
    assert gc.execute_action('myaction_copy') == "A variable"


