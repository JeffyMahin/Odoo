{
    'name' : 'Test Hospital Management',
    'version' : '1.0',
    'summary': 'Hospital Test Summary',
    'sequence': 10,
    'description': '''Hospital Test Description''',
    'category': 'Productivity',
    'website': 'https://www.google.com/',
    'images': [],
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hospital_patient.xml',
        'views/hospital_doctor.xml',
        'views/sale.xml'

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'author': "Mahin",
}
