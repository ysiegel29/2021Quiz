
from address import Address


class User:
    def __init__(self, firstname, lastname, age, address):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

        if isinstance(address, Address):
            self.address = address
        else:
            print('Not a valida address')


