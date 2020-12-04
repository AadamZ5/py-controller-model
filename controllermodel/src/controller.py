"""
The file contains the code for the GenericController class.
"""

import inspect
import functools
from typing import Optional

from .controllerinterface import ControllerInterface

class GenericController(ControllerInterface):
    """
    The base type Controller for a model. This implementation is barebones and very generic, but still perfectly usable. 
    """

    _registered_classes = {}   # Dict of {
                                #           registering_controller {
                                #               klass: {
                                #                   action: method        
                                #               }
                                #           }
                                #       }

    def __init__(self, instance_of_class: Optional[object] = None):
        self._cls_instance = None
        self._func_set = None
        if instance_of_class != None:
            self.connect_instance(instance_of_class)

    def connect_instance(self, instance_of_class):
        """
        Connect an instance to the action definitions.
        """

        if not instance_of_class.__class__.__qualname__ in self.__class__._registered_classes.get(self.__class__, {}):
            raise Exception(f"Class {instance_of_class} has not been regestered with this controller class (yet?)!")

        self._cls_instance = instance_of_class
        self._func_set = self._registered_classes[self.__class__][instance_of_class.__class__.__qualname__]

    @classmethod
    def register_model(cls, _reg_cls):
        """
        This is a decorator funciton.

        Does nothing right now.
        Probably won't do anything for awhile. I see no use.
        """

        # This doesn't get called until all of the functions are done being defined
        # in the potential model class. 

        # The biggest challenge is linking the instance to its type's registered actions. 
        # When this function is used as a decorator 
        return _reg_cls

    @classmethod
    def register_action(cls, _func=None, *args, action=None, description=None, **kw):
        """
        This is a decorator function.

        Will register a function as an action to do stuff on this controller.

        Tries to grab the action name from the function name, and a description from the functions 
        docstring.
        """

        print(str(_func))

        def wrapper_func(func):

            # `nonlocal` beacause see: https://stackoverflow.com/questions/2609518/unboundlocalerror-with-nested-function-scopes
            nonlocal action
            nonlocal description
            nonlocal cls

            print(action)
            print(description)
            print(cls)

            if action == None:
                try:
                    action = func.__name__ # Try and get a name from the function itself if they didn't supply one.
                except AttributeError:
                    raise TypeError("Object is not a named function!") #! We don't like lambdas! (Can you even decorate those?)
            if description == None:
                description = inspect.getdoc(func) # See if we can grab the docstring if one exists.

            # Get the owning class's qualifying name
            owning_class = None
            try:
                qn = str(func.__qualname__)             # A.B.cmethod
                qn = qn.replace(func.__name__, '')      # A.B.
                if qn[-1] == '.':                       # A.B
                    qn = qn[:-1]
                owning_class = qn                       # 🙂
            except AttributeError:
                raise Exception("Function does not have a valid qualifying name! Is this function a member of a class?")
            if owning_class == '':
                #TODO: Add ability for class-less functions / top-level qualnames to be registered!
                raise Exception("Function does not have a valid qualifying name! Is this function a member of a class?")
            if not cls in cls._registered_classes:
                cls._registered_classes[cls] = {}
            cls._registered_classes[cls][owning_class] = {action: func}
            return func

        if _func == None:
            print("Returning un-parameterized dec-func")
            return wrapper_func # If the decorator was called with keyword parameters, the _func variable isn't supplied. Just return this function to be applied.
        else:
            print("Returning barebones dec-func")
            return wrapper_func(_func) #If the decorator was called without keywords, the function we are targeting is implicitly supplied.

    def execute_action(self, action: str, *a, **kw):
        if action in self._func_set:
            return self._func_set[action](self._cls_instance, *a, **kw)
        else:
            return None
