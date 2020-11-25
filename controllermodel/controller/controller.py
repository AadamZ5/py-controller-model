import inspect
import functools
from typing import Dict, T, Callable

from .controllerinterface import ControllerInterface

class GenericController(ControllerInterface):
    """
    Creates a controller for a model. 
    """

    def __init__(self, model_instance):
        self._class_types = {} #A dictionary of `class: dict[action, function]`

    @classmethod
    def register_model(cls, _reg_cls: T):
        #TODO: Register class type for correlation later!

        # This doesn't get called until all of the functions are done being defined
        # in the potential model class. 

        print(_reg_cls)

        # The biggest challenge is linking the instance to its type's registered actions. 
        # We will have to register one model (and treat subsequent registers as overwrites)
        # to correlate to the registered actions. 
        #!Is there a better way??

        pass

    def register_action(self, _func=None, *args, action=None, description=None, **kw):
        """
        Eventually, will register a function as an action to do stuff on this controller.

        Tries to grab the action name from the function name, and a description from the functions 
        docstring.
        """

        #TODO: Get the instance the function was registered from if possible! We can't call unbound functions! 
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

            # self._actions[action] = (class_type, func)
            # self._descriptions[action] = description
            return func

        if _func == None:
            return wrapper_func
        else:
            return wrapper_func(_func, action=action, description=description)
