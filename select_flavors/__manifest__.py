{
    'name': 'select_flavors',
    'version': '1.0',
    'depends': ['point_of_sale', 'product'], # Añadimos 'product' por seguridad
    'data': [
        'views/product_template_views.xml', # EL BACKEND SÍ VA AQUÍ
    ], 
    'assets': {
        'point_of_sale._assets_pos': [
            'select_flavors/static/src/js/product_configurator_patch.js',
            'select_flavors/static/src/xml/product_configurator_templates.xml',
        ],
    },
    'installable': True,
}