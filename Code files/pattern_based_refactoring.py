# pylint: skip-file
from abc import ABC, abstractmethod


# ------------------------------------------------------------------------------
# Encapsulate subclasses with creation Methods

class Person(ABC):
    '''Common interface for an external person to the business.'''
    @abstractmethod
    def contact(self):
        pass

    @staticmethod
    def new_lead(self):
        return Lead()

    @staticmethod
    def new_customer(self):
        return Customer()


person = Person.new_lead()  # returns a Lead() object
person.contact()


class Lead(Person):

    def __init__(self):
        '''Do not call, use Person.new_lead() instead'''
        super(Lead, self).__init__()

    def contact(self):
        print('Hi lead.')


class Customer(Person):

    def __init__(self):
        '''Do not call, use Person.new_customer() instead'''
        super(Customer, self).__init__()

    def contact(self):
        print('Hi, customer.')

# ------------------------------------------------------------------------------
# Removing multiple checks for None in your Python code


class AccountExecutive:

    def reach_out(self, message):
        '''AE reaches out to his accounts'''
        pass


class NullAccountExecutive(AccountExecutive):

    def __init__(self, primary_contact):
        self.primary_contact = primary_contact

    def reach_out(self, message):
        send_email(self.primary_contact)


class Company:
    account_exec = NullAccountExecutive()


def call_customer(company):
    company.account_exec.reach_out('Hello!')


def send_email(target):
    pass


# ------------------------------------------------------------------------------
# Python refactoring using conditionals


def pass_persona_downstream(company_size, industry, product):
    # multiple conditionals that have the same result
    if is_within_ideal_profile(company_size, industry, product):
        # merged logic
        pass


def is_within_ideal_profile(company_size, industry, product):
    is_right_size = company_size < 100 or company_size > 100000
    return is_right_size and industry != 'training' and product != 'SaaS'


class Product:
    '''Replace conditional with subclasses'''

    def get_price(self):
        pass


class SelfService(Product):

    def get_price(self):
        return self.base_price


class Discounted(Product):

    def get_price(self):
        return self.base_price * self.discount


class Enterprise(Product):

    def get_price(self):
        return self.base_price * self.discount + self.service_revenue


# later on..
price = product.get_price()