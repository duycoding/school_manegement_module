# -*- coding: utf-8 -*-
{
    'name': 'Test Module 1',
    'summary': 'Đây là module test thử lần 1',
    'version': '1.0',
    'sequence': -100,
    'website': 'https://www.yourwebsite.com',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        # Add your data files here
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'data/student_demo.xml',
    ],
    'demo': [
        # Add your demo files here

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
