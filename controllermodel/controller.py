"""
The file contains the code for the GenericController class.
"""

import inspect
import functools
from typing import Optional, Union, List, Tuple

from .controllerinterface import ControllerInterface

class GenericController(ControllerInterface):
    """
    The base type Controller for a model. This implementation is barebones and very generic, but still perfectly usable. 
    """

    _registered_classes = {}   # Dict of {
                                #           registering_controller: {
                                #               klass: {
                                #                   action: func_name        
                                #               }
                                #           }
                                #       }

    def __init__(self, instance_of_class: Optional[object] = None):
        self._func_set = {} # Dict of {action: class_qualname}
        self._class_instances = {}
        if instance_of_class != None:
            self.connect_instance(instance_of_class)

    def connect_instance(self, instance_of_class: Union[List[object], Tuple[object], object], *additional_instances: Tuple[object]):
        """
        Connect an instance to the action definitions.
        """

        if len(additional_instances) > 0:
            instance_of_class = [instance_of_class, *additional_instances]

        if(isinstance(instance_of_class, list) or isinstance(instance_of_class, tuple)):
            for i in instance_of_class:
                self.connect_instance(i)
        else:
            if instance_of_class == None:
                raise TypeError("Can't connect instance 'None' type!")

            if not instance_of_class.__class__.__qualname__ in self.__class__._registered_classes.get(self.__class__.__qualname__, {}):
                raise Exception("Class '{0}' has not been regestered with this controller class (yet?)!".format(instance_of_class))

            self._class_instances[instance_of_class.__class__.__qualname__] = instance_of_class
            func_names = self._registered_classes[self.__class__.__qualname__][instance_of_class.__class__.__qualname__].keys()

            for n in func_names:
                self._func_set[n] = (instance_of_class.__class__.__qualname__, self._registered_classes[self.__class__.__qualname__][instance_of_class.__class__.__qualname__][n]) # Tuple of (class_name, unbound_func)
            

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
    def _check_action_exists(cls, action_name):
        if not cls.__qualname__ in cls._registered_classes:
            return 

        for registered_class in cls._registered_classes[cls.__qualname__].keys():
            actions = cls._registered_classes[cls.__qualname__][registered_class].keys()
            if action_name in actions:
                conflicting_action = str(next((x for x in actions if x == action_name), '[Unknown]'))
                raise ValueError("Action name '{0}' has already been registered on controller '{1}'!\nConflicting registration with action '{2}' from class '{3}'.".format(action_name,cls.__qualname__,conflicting_action,registered_class))


    @classmethod
    def register_action(cls, _func=None, *args, action=None, description=None, **kw):
        """
        This is a decorator function.

        Will register a function as an action to do stuff on this controller.

        Tries to grab the action name from the function name, and a description from the functions 
        docstring.
        """

        def wrapper_func(func):

            if not callable(func):
                raise TypeError("Object {0} is not callable!".format(func))

            # `nonlocal` beacause see: https://stackoverflow.com/questions/2609518/unboundlocalerror-with-nested-function-scopes
            nonlocal action
            nonlocal description
            nonlocal cls

            if action == None:
                try:
                    action = func.__name__ # Try and get a name from the function itself if they didn't supply one.
                except AttributeError:
                    raise TypeError("Object {0} is not a named function!".format(func)) #! We don't like lambdas! (Can you even decorate those?)
            if description == None:
                description = inspect.getdoc(func) # See if we can grab the docstring if one exists.

            # Make sure there are no conflicting action names registered on this specific controller.
            cls._check_action_exists(action) # This will except if there is. 

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
            if not cls.__qualname__ in cls._registered_classes:
                cls._registered_classes[cls.__qualname__] = {}
            if not owning_class in cls._registered_classes[cls.__qualname__]:
                cls._registered_classes[cls.__qualname__][owning_class] = {}
            cls._registered_classes[cls.__qualname__][owning_class][action] = func.__name__
            return func

        if _func == None:
            return wrapper_func # If the decorator was called with keyword parameters, the _func variable isn't supplied. Just return this function to be applied.
        else:
            return wrapper_func(_func) # If the decorator was called without keywords, the function we are targeting is implicitly supplied.

    def execute_action(self, action: str, *a, **kw):
        if action in self._func_set: # Find out where the action came from. Which class?
            class_type, func_name = self._func_set[action] # Get the class name, and the function name   
            class_instance = self._class_instances.get(class_type, None) # Try to get an instance
            if class_instance:
                func = getattr(class_instance, func_name, None) # Get the actual *bound* function on the class
                if func:
                    return func(*a, **kw) # The instance is automatically passed in on this bound class function
        return None
