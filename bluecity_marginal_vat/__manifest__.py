# -*- coding: utf-8 -*-
{
    'name': 'Marginal VAT',
    'description': 'Marginal VAT calculation using Danish model',
    'category': 'Sale',
    'version': '15.0.1.0.0',
    'author' : 'Blue City A/S',
    'website' : 'www.bluecity.dk',
    'depends': [
        'sale_management', 
        'purchase', 
        'sale_stock', 
        'account',
        'select_serial_number',
    ],
    'data': [
        'data/account_fiscal_position_data.xml',
        'views/purchase_order_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_move_line_views.xml',
        'views/account_tax_views.xml',
        'views/account_fiscal_position_views.xml',
        'views/stock_production_lot_views.xml',
    ],
}   