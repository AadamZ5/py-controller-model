"""
The file contains the code for the GenericController class.
"""

import inspect
import functools
from typing import Dict, T, Callable

from .controllerinterface import ControllerInterface

class GenericController(ControllerInterface):
    """
    The base type Controller for a model. This implementation is barebones and very generic, but still perfectly usable. 
    """

    _registered_classes = {}   # Dict of {
                                #           klass: {
                                #               action: method        
                                #           }
                                #       }

    def __init__(self, instance_of_class: T):
        print(GenericController._registered_classes)
        if not instance_of_class.__class__.__qualname__ in GenericController._registered_classes:
            raise Exception(f"Class {instance_of_class} has not been regestered with this controller class (yet?)!")

        self._cls_instance = instance_of_class
        self._func_set = self._registered_classes[instance_of_class.__class__.__qualname__]

    @classmethod
    def register_model(cls, _reg_cls: T):
        """
        This is a decorator funciton.

        Does nothing right now.
        Probably won't do anything for awhile. I see no use.
        """

        # This doesn't get called until all of the functions are done being defined
        # in the potential model class. 

        #cls._registered_classes[str(_reg_cls.__qualname__)] don't do nothin

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

        #If we can figure out how to grab class instances, we can hotwire them into the function calls.

        def wrapper_func(func, *a, action=None, description=None):
            print(f"Registering function {func}")

            if action != None:
                print(f"Overriding action name to {action}")
            else:
                try:
                    action = func.__name__
                except AttributeError:
                    raise TypeError("Object is not a named function!")
            if description != None:
                print(f"Overriding description to {description}")
            else:
                description = inspect.getdoc(func)

            owning_class = None
            try:
                qn = str(func.__qualname__)
                qn = qn.replace(func.__name__, '')
                if qn[-1] == '.':
                    qn = qn[:-1]
                owning_class = qn
            except AttributeError:
                raise Exception("Function does not have a valid qualifying name! Is this function a member of a class?")
            if owning_class == '':
                raise Exception("Function does not have a valid qualifying name! Is this function a member of a class?")
            print(f"Owning class is {owning_class}")
            cls._registered_classes[owning_class] = {action: func}

            return func

        if _func == None:
            return wrapper_func
        else:
            return wrapper_func(_func, action=action, description=description)

    def execute_action(self, action: str, *a, **kw):
        if action in self._func_set:
            return self._func_set[action](self._cls_instance, *a, **kw)
        else:
            return None
