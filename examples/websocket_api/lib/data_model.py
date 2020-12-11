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
        self.persons = [] list
        self.special_number = 23

    @WebsocketController.register_action
    def add_employee(self, name, age, employee_id):
        new_employee = Employee(name, age, employee_id)
        self.persons.append(new_employee)
        return {'employee': new_employee}

    @WebsocketController.register_action
    def add_customer(self, name, age):
        new_customer = Customer(name, age)
        self.persons.append(new_customer)
        return {'customer': new_customer}

    @WebsocketController.register_action
    def get_persons(self):
        return self.persons



    