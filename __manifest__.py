# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Amaroo Sale Customization',
    'version' : '1.0',
    'summary': 'Product check availability based on Quantity Available Unreserved',
    'sequence': 30,
    'description': """
Sale order line Product check availability feature based on Quantity Available Unreserved value
    """,
    'category': 'Custom',
    'author' : 'Amaroo Solutions',
    'website': 'http://amaroosolutions.co.uk/',
    'images' : [],
    'depends' : ['sale_stock', 'stock_available_unreserved'],
    'data': [
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
