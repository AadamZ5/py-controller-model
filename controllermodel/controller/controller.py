from .controllerinterface import ControllerInterface


class GenericController(ControllerInterface):

    def register_action(self, _func=None, *args, action=None, description=None, **kw):
        """
        Eventually, will register a function as an action to do stuff on this controller.
        """

        def wrapper_func(func):
            print(f"Working with function {func}")
            if func.__name__:
                print(f"\tName: {func.__name__}")
            return func

        if _func == None:
            return wrapper_func
        else:
            return wrapper_func(_func)
