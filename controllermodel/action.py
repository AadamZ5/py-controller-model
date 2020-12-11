import inspect

class Action:
    """
    Holds meta-data about a registered action.
    """
    def __init__(self, func: object, action=None, description=None):
        # We shouldn't store `func` because we shouldn't use it. The controller uses `getattr` on the instance class registered later.
        # The reason for this is because if the function is reassigned or changed sometime later after we've registered it, we want to call
        # the updated function, not the old function that was initially given. `getattr` is the best way to make sure this happens.
        if not callable(func):
            raise TypeError("Object {0} is not a valid callable object. It can not be used as an action.".format(func))
        
        try:
            self.func_name = func.__name__
            self.func_qualname = func.__qualname__
        except AttributeError:
            raise TypeError("Object {0} is not a named function!".format(func))

        if action == None:
            try:
                action = func.__name__ # Try and get a name from the function itself if they didn't supply one.
            except AttributeError:
                raise TypeError("Object {0} is not a named function!".format(func))
        if description == None:
            description = inspect.getdoc(func) # See if we can grab the docstring if one exists.

        self.action = action
        self.description = description
        self.parameters = []
        self.argspec = inspect.getfullargspec(func) # Let's write in the documentation about typing arguments!
        #TODO: Use argspec for something!

    
        
        