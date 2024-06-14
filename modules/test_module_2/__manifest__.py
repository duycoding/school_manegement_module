# library_management/__manifest__.py
{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Module quản lý thư viện',
    'sequence': -100,
    'description': """
        Mô-đun quản lý thư viện đơn giản
    """,
    'category': 'Uncategorized',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
