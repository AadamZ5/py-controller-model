# py-controller-model

Simplifies arbitrary API creation by leaving definition and binding in-code. 

Goals:
- [ ] Bind a controller to a model
- [ ] Register using decorators 
- [ ] Easy documentation (and basic introspection?)

## Installation

Clone this repository, then when inside of the directory, install with `pip install .`

## Example usage

### Useage of the generic implementation

```python
import controllermodel as cm

class A:
    def __init__(self):
        self.a = "A variable"

    @cm.GenericController.register_action(action="action")
    def myaction(self):
        print(self.a)

a = A()
gc = cm.GenericController(a)

#Now wire in gc to an API endpoint class such as a websocket to easily and quickly map API calls.
```

### Noticing how a derived class behaves

```python
import controllermodel as cm

class SpecificController(cm.GenericController):
    def __init__(self, instance_of_class):
        super().__init__(instance_of_class)

    def special_method(self):
        print(self._registered_classes)

@SpecificController.register_model
class A:
    def __init__(self):
        self.a = "A variable"

    @SpecificController.register_action
    def myaction(self):
        print(self.a)



print(cm.GenericController._registered_classes)     # Although this variable isn't to be used by you,
print(SpecificController._registered_classes)       # it is worth noting that these will be the same value.

a = A()
sc = SpecificController(a)
gc = cm.GenericController(a)    # <<-- This will raise an Exception! We have not registered any
                                #       functions of class A to `GenericController`

sc.special_method()
sc.execute_action('myaction')

```

### Notes

`GenericController` is designed to be inherited from in your own controller. The important function to consider is `GenericController.execute_action` which is the function that looks up the corresponding model function to call.

## Contributing

Please feel free to open an issue or pull request with your ideas and intentions! Any help is greatly appreciated! 