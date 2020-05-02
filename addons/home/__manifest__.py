# -*- coding: utf-8 -*-
{
    'name': 'Home',
    'category': 'Tools',
    'summary': 'Permite la bandeja de inicio por defecto',
    'description': """
        Este módulo permite establecer la bandeja de inicio por defecto de la plataforma.
    """,
    'depends': ['base'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'application': True,
    'auto_install': True,
}
