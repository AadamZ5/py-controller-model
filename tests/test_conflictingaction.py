import pytest

from controllermodel import GenericController

def test_conflictingaction_sameclass():
    with pytest.raises(ValueError):
        @GenericController.register_model
        class A:
            def __init__(self):
                self.a = "A variable"

            @GenericController.register_action(action="action")
            def myaction1(self):
                print(self.a)
                return self.a

            @GenericController.register_action(action="action")
            def myaction2(self):
                print(self.a)
                return self.a

def test_conflictingaction_diffclass():
    with pytest.raises(ValueError):
        @GenericController.register_model
        class A:
            def __init__(self):
                self.a = "A variable"

            @GenericController.register_action(action="action")
            def myaction(self):
                print(self.a)
                return self.a

        @GenericController.register_model
        class B:
            def __init__(self):
                self.b = "B variable"

            @GenericController.register_action(action="action")
            def myaction(self):
                print(self.b)
                return self.b
    
