# -*- coding: utf-8 -*-
{
    'name': 'Addenda Producto',
    'version': '1.0.0.1.0',
    'author': 'HomebrewSoft',
    'website': '',
    'depends': [
        'product',
        'openacademy',
        'account',
    ],
    'data': [
        # security
        'security/groups.xml',
        'security/ir.model.access.csv',
        # data
        # demo
        # reports
        # views
        'views/product_template.xml',
        'views/product_template_addendum.xml',
        'views/account_move.xml',
    ],
}
