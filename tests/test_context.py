import pytest

from controllermodel import GenericController, GenericControllerContext

@GenericController.register_model
class A:
    def __init__(self):
        self.a = "A variable"

    @GenericController.register_action(action="actionx")
    def myaction(self, *a, p1=None, _context=None):
        print(self.a, a, p1)
        print(_context)
        return (self.a, a, p1, _context)

def test_context():
    a = A()
    gc = GenericController(context_class=GenericControllerContext)
    gc_ctxt = GenericControllerContext()
    gc_ctxt.prop = "Context property"
    gc.connect_instance(a)
    assert gc.execute_action('actionx', "Parameter 1", "Parameter 2", _context=gc_ctxt) == ("A variable", ("Parameter 1", "Parameter 2"), None, gc_ctxt)
    assert gc.execute_action('actionx', _context=gc_ctxt, **{'p1': "Keyword 1"}) == ("A variable", (), "Keyword 1", gc_ctxt)
    assert gc.execute_action('actionx', "Parameter 1", "Parameter 2", _context=gc_ctxt, **{'p1': "Keyword 1"}) == ("A variable", ("Parameter 1", "Parameter 2"), "Keyword 1", gc_ctxt)

def test_no_context():
    a = A()
    gc = GenericController(context_class=GenericControllerContext)
    gc_ctxt = GenericControllerContext()
    gc_ctxt.prop = "Context property"
    gc.connect_instance(a)
    assert gc.execute_action('actionx', "Parameter 1", "Parameter 2", _context=None) == ("A variable", ("Parameter 1", "Parameter 2"), None, None)
    assert gc.execute_action('actionx', _context=None, **{'p1': "Keyword 1"}) == ("A variable", (), "Keyword 1", None)
    assert gc.execute_action('actionx', "Parameter 1", "Parameter 2", _context=None, **{'p1': "Keyword 1"}) == ("A variable", ("Parameter 1", "Parameter 2"), "Keyword 1", None)
