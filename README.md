# py-controller-model

Simplifies arbitrary API creation by leaving definition and binding in-code. 

Goals:
- [ ] Bind a controller to a model
- [ ] Register using decorators 
- [ ] Easy documentation (and basic introspection?)

## Installation

Clone this repository, then when inside of the directory, install with `pip install .`

## Example usage

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

### Notes

`GenericController` is designed to be inherited from in your own controller. The important function to consider is `GenericController.execute_action` which is the function that looks up the corresponding model function to call.

## Contributing

Please feel free to open an issue or pull request with your ideas and intentions! Any help is greatly appreciated! 