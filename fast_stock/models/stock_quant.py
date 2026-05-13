from odoo import models, fields, api

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    def action_validate_panaderia(self):
        for record in self:
            # Aplica el cambio absoluto de inventory_quantity
            record.action_apply_inventory()
            
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }