# -*- coding: utf-8 -*-
{
    'name': 'Home',
    'category': 'Tools',
    'summary': 'Centralize your address book',
    'description': """
This module gives you a quick view of your contacts directory, accessible from your home page.
You can track your vendors, customers and other contacts.
""",
    'depends': ['base', 'mail'],
    'data': [
        'views/contact_views.xml',
    ],
    'application': True,
}
