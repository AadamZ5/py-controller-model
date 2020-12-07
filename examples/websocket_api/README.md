# Simple websocket API endpoint

This example demonstrates how this library can be used to simplify a simple websocket API endpoint.

## Parts

 - `lib/data_model.py` This is the DataModel of our example. It holds and manipulates our data. This is what we want our API endpoint to control.
 - `lib/websocket_endpoint.py` This is our API that controls our DataModel. 
 - `app.py` This is the application file to run.
 - Port `7033` is used for this example.

## Getting started

Once inside of the directory, install the requirements for this eample with `pip install -r requirements.txt` or `python3 -m pip install -r requirements.txt` if `pip` isn't in your PATH.

Then, run the project with `python3 app.py`.

In a separate terminal, run `python3 -m websockets ws://127.0.0.1:7033`. If you are met with a websockets prompt, great!

Write `{"action": "add_customer", "data": {"name": "Guy Person", "age": 23}}` and send it to the websocket. If all is well, you should be greeted back with a JSON object of your customer.

Next, try again with `"add_employee"` instead and see your results!

Finally, try adding another action like "add_manager" to see what it's like to use the library!

## Notes about design

In our design, it is worth noting that `WebsocketController` does not hold any special logic to figure out where to send what request. This is all taken care of in `execute_action` (from `GenericController`). This shows the benefit from this library, being able to simply register API functions right next to the actual defenition of the code. 

Again, all of our API controller routing is actually done on the DataModel, which makes it easier to maintain code. 

```python
class DataModel:
    def __init__(self):
        self.persons = []

    @WebsocketController.register_action # This will register an action "add_employee" that we can then call from a client websocket.
    def add_employee(self, name, age, employee_id):
        new_employee = Employee(name, age, employee_id)
        self.persons.append()
        return {'employee': new_employee} # This gets sent back through our websocket controller. 
                                          # The WebsocketController class decides how to handle the data we send back.
...
```

## Important concepts

`WebsocketController` contains only the additional logic for dealing with our websocket. For example, the additional logic is *only* for parsing the data from a websocket, and returning results. In this instance, that additional logic specifically is utilizing `jsonpickle` to decode incoming JSON messages, and send back out JSON messages.

Underneath `WebsocketController`, we have our `GenericController` to control registering actions, and finding them later on. However, you'll notice that we still use `@WebsocketController.register_action` to register actions. This is so we can keep API endpoints separate. For instance, we could also have an `HttpController` that would controll data coming in on HTTP. We wouldn't want `WebsocketController` and `HttpController` to see eachother's actions. Thus, when you have multiple API endpoints in the same app, they should both be their own unique class. 

To register the same function from the same model, perhaps with different action names, to two or more controllers you've made, simply add the decorators to your function as so:
```python

@WebsocketController.register_action(action="add_employee") # This will register an action only on WebsocketController
@HttpController.register_action(action="ADD_EMPLOYEE") # This will register an action only on HttpController            
def add_employee(self, name, age, employee_id):        # [!] HttpController isn't actually defined in this example project! [!] 
    new_employee = Employee(name, age, employee_id)
    self.persons.append()
    return {'employee': new_employee} # This gets sent back through our websocket controller. 
                                      # The WebsocketController class decides how to handle the data we send back.
...
```
