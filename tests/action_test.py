from controllermodel import GenericController

@GenericController.register_model
class A:
    def __init__(self):
        self.a = "A variable"

    @GenericController.register_action(action="action")
    def myaction(self):
        print(self.a)
        return self.a



print(GenericController._registered_classes)


def test_action():
    a = A()
    gc = GenericController(a)
    assert gc.execute_action('action') == "A variable"
