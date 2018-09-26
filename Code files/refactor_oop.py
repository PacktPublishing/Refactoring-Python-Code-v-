import collections


class Person:
    company_website = ''
    area_code = '+44'
    number = '01212158624'

    def __init__(self):
        Telephone = collections.namedtuple('Telephone', ['area_code', 'number'])
        self.tel = Telephone(area_code='+44', number='285491510')

    def get_company_website_extension(self):
        result = self.company_website.replace('/', '').split('.')
        if len(result) > 1:
            return result[-1]
        else:
            print('Not a valid domain')
            return ''

    def dial(self):
        return self.tel.area_code + self.tel.number


class Customer(Person):
    stage = 'customer'


class Lead(Person):
    stage = 'lead'


class Opportunity(Person):
    stage = 'opportunity'


BASE_PRICE = 100
TAX_RATE = 0.75


class Employee:

    def notify(self, message):
        pass


class Company:
    website = ''
    size = 0
    industry = ''
    employees = []

    # 4.3
    def email_key_employee(self, message):
        self.employees[0].notify(message)

    def get_key_employee(self):
        return self.employees[0]


# can use mixins to factor out the pricing algorithm
class SmallMediumBusiness(Company):

    def send_notification(self, email_func):
        email_func(self.employees[0].email)

    def send_notification_delegate(self, email_func, message):
        self.email_key_employee(message)

    def send_notification_no_middlemen(self, message):
        self.get_key_employee().notify(message)

    def get_pricing(self, units):
        base, tax = self.pricing(units)
        return base * tax

    def pricing(self, units):
        total_price = BASE_PRICE * units
        base = total_price * 0.8
        tax = base * TAX_RATE * 0.8
        return base, tax


class Enterprise(Company):

    account_executive = {}

    def send_notification(self, email_func):
        email_func(self.account_executive['email'])

    def get_pricing(self, units):
        base = BASE_PRICE * units
        tax = base * TAX_RATE
        return base * tax
