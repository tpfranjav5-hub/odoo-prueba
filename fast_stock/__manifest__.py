{
    'name': 'Stock Rápido',
    'version': '1.0',
    'category': 'Inventory',
    'depends': ['stock'],
    'data': [
        'views/stock_view.xml',
    ],
    # No hace falta añadir los .py aquí, Odoo los lee mediante el __init__
    'installable': True,
    'application': True,
}