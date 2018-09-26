from abc import abstractmethod, ABCMeta

import util


class SuperCustomer(metaclass=ABCMeta):
    def __init__(self):
        self.name = name

    def __str__(self):
        return '<Customer {}>'.format(self.name)

    @abstractmethod
    def switch_company(self, new_company):
        pass


class Customer(SuperCustomer):

    def __init__(self, name, email, company):
        self.first_name = ''
        self.last_name = ''
        self.name_to_first_last(name)

        self.email = email
        self.company = company

    def name_to_first_last(self, name):
        if len(name.split(' ') > 1):
            self.first_name = util.get_first_name(name)
        else:
            self.first_name = ''
        if len(name.split(' ') > 1):
            self.last_name = name.split(' ')[1]
        else:
            self.last_name = name

    def add_email(self, new_email):
        if isinstance(self.email, str):
            self.email = [self.email, new_email]
        else:
            self.email.append(new_email)

    def switch_company(self, new_company):
        self.company = new_company


