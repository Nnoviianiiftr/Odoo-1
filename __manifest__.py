# __manifest__.py
# -*- coding: utf-8 -*-
{
    'name': "Dental Care",
    'summary': "Dental care module for managing services, doctors, patients, and appointments",
    'description': "Custom module for dental care management in Odoo.",
    'author': "Noviani Fitri",
    'website': "https://https://odoo.narloci.my.id/",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'dental'],
    'data': [
        'views/services_view.xml',
        'views/doctors_view.xml',
        'views/patients_view.xml',
        'views/appointments_view.xml',
    ],
    'installable': True,
    'application': True,
}