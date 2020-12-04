import pytest

from controllermodel import GenericController

@GenericController.register_model
class A:
    def __init__(self):
        self.a = "A variable"

    @GenericController.register_action(action="action1")
    def myaction(self, *a, p1=None):
        print(self.a, a, p1)
        return (self.a, a, p1)

@GenericController.register_model
class B:
    def __init__(self):
        self.b = "B variable"

    @GenericController.register_action(action="action2")
    def myaction(self, *a, p1=None):
        print(self.b, a, p1)
        return (self.b, a, p1)

def test_action():
    a = A()
    b = B()
    gc = GenericController()
    gc.connect_instance(a)
    gc.connect_instance(b)
    assert gc.execute_action('action1', "Parameter 1", "Parameter 2") == ("A variable", ("Parameter 1", "Parameter 2"), None)
    assert gc.execute_action('action2', "Parameter 1", "Parameter 2") == ("B variable", ("Parameter 1", "Parameter 2"), None)
    assert gc.execute_action('action1', **{'p1': "Keyword 1"}) == ("A variable", (), "Keyword 1")
    assert gc.execute_action('action2', **{'p1': "Keyword 1"}) == ("B variable", (), "Keyword 1")
    assert gc.execute_action('action1', "Parameter 1", "Parameter 2", **{'p1': "Keyword 1"}) == ("A variable", ("Parameter 1", "Parameter 2"), "Keyword 1")
    assert gc.execute_action('action2', "Parameter 1", "Parameter 2", **{'p1': "Keyword 1"}) == ("B variable", ("Parameter 1", "Parameter 2"), "Keyword 1")