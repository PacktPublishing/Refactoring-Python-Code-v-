'''A badly written, example CRM app.'''
import itertools
import os
import sys

from sklearn import linear_model
from sklearn.model_selection import train_test_split


def read_this_file(filename):  # unneeded
    with open(filename, 'rb') as f:
        return f.readlines()


# split this up in 3.1
def import_leads(leads_file):  # function that is too long
    '''Import file, process leads, enrich leads, return processed_leads'''
    processed_leads = []

    try:
        with open(leads_file, 'rb') as f:
            leads = f.readlines()

            for lead in leads:
                processed_lead = {}
                processed_lead['first_name'] = lead.split()[0]
                processed_lead['last_name'] = lead.split()[0]
                processed_lead['email'] = lead.split()[0]
                processed_lead['company'] = lead.split()[0]
                processed_lead['twitter'] = lead.split()[0]
                processed_lead['website'] = lead.split()[0]
                processed_leads.append(processed_lead)

            for p_lead in processed_leads:
                p_lead['first_name'] = p_lead['first_name'].replace(' ', '')
                p_lead['last_name'] = p_lead['last_name'].lower()

                if 'gmail' in p_lead['email']:
                    print('Importing gmail')
                elif 'hotmail' in p_lead['email']:
                    print('Importing hotmail')
                else:
                    print('Custom mail server.')

                p_lead['company'] = p_lead['company']
                p_lead['twitter'] = p_lead['twitter'].replace('@', '')
                p_lead['website'] = p_lead['website'].replace('https://', '')

    except OSError:
        print('Cannot open file')

    return processed_leads


class Lead:
    touchpoints = []
    company_size = ''
    _company_website = ''
    days_since_last_post = 0
    discount = 1

    def get_lead_score(self):
        return 1 if self.is_active() else 0

    # 3.2: a method that should be merged into get_lead_score
    def is_active(self):
        return self.days_since_last_post < 5

    # 3.2: mrr should be inlined to the return statement
    def get_lifetime_value(self, product):
        mrr = product.base_price() * self.discount
        return mrr * 12


class Customer:
    company_size = ''
    lead = Lead()
    company_website = ''

    def __init__(self, lead):
        # One class uses the internal fields and methods of another class.
        self.company_size = lead.company_size
        self.company_website = lead._company_website
        self.lead = lead


# 3.3 Replace complex expressions with inner function calls
class CRMImportEntry:
    '''Entry imported from our legacy CRM.'''
    def __init__(self):
        imported_data = {
            'name': {
                'first': 'John',
                'last': 'Smith'
            },
            'company': 'ACME',
            'deals': [13435, 33456]
        }

        def get_name_from_import(data):
            if 'name' in data:
                return data['name']
            else:
                print('Name not found.')
                return dict(first='', last='')

        self.first_name = get_name_from_import(imported_data).get('first', '')
        self.last_name = get_name_from_import(imported_data).get('last', '')
        self.num_deals = len(imported_data.get('deals', []))


def convert_lead(lead):
    if lead.company_size == 'smb':
        send_smb_funnel()
    elif lead.company_size == 'mid_market':
        send_mid_market_funnel()
    elif lead.company_size == 'enterprise':
        log_manual_sales_follow_up()
    else:
        print('Wrong lead company type!')


def send_smb_funnel(services=''):
    client = services.email.client('transactional', region='eu-ireland')
    response = client.send_email(
        destination='test@gmail.com',
        message={
            'body': {'Text': {'Hello small business!'}},
            'subject': {'Text': {'Buy our stuff!'}}
        },
        source='refactoring@course.com'
    )
    print(response)


def send_mid_market_funnel(services=''):
    client = services.email.client('transactional', region='eu-ireland')
    response = client.send_email(
        destination='test@gmail.com',
        message={
            'body': {'Text': {'Hello medium sized business!'}},
            'subject': {'Text': {'Buy our stuff!'}}
        },
        source='refactoring@course.com'
    )
    print(response)


def log_manual_sales_follow_up(services=''):
    client = services.email.client('transactional', region='eu-ireland')
    response = client.send_email(
        destination='internal.sales@course.com',
        message={
            'body': {'Text': {'Go say hello to this business!'}},
            'subject': {'Text': {'Buy our stuff!'}}
        },
        source='refactoring@course.com'
    )
    print(response)


# 3.4
def prioritize_lead(lead):
    is_right_size = (lead.company_size > 100) and (lead.company_size < 100000)
    is_dotcom = lead.company_website.endswith('.com')
    is_new_lead = len(lead.touchpoints) == 0
    if is_right_size and is_dotcom and is_new_lead:
        lead.priority = 100
