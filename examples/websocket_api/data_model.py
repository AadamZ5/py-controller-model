from .websocket_endpoint import WebsocketController

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Customer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

class Employee(Person):
    def __init__(self, name, age, employee_id):
        self.employee_id = employee_id
        super().__init__(name, age)

@WebsocketController.register_model
class DataModel:
    def __init__(self):
        self.persons = []

    @WebsocketController.register_action
    def add_employee(self, name, age, employee_id):
        self.persons.append(Employee(name, age, employee_id))

    @WebsocketController.register_action
    def add_customer(self, name, age):
        self.persons.append(Customer(name, age))

    