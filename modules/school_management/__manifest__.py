{
    'name': "School Management",
    'version': '1.0',
    'depends': ['base'],
    'author': "Author Name",
    'category': 'Uncategorized',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/student_views.xml',
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
}