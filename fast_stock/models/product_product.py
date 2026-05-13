from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProductProduct(models.Model):
    _inherit = 'product.product'

    # Campo donde escribes lo que has contado
    new_stock_quantity = fields.Float(string='Cantidad Real', default=0.0)

    def action_validate_panaderia_bulk(self):
        # 1. Buscamos la ubicación 'WH/Stock' (Interna)
        location = self.env['stock.location'].search([('usage', '=', 'internal')], limit=1)
        
        if not location:
            raise UserError(_("No se ha encontrado una ubicación interna para ajustar el stock."))

        for product in self:
            # Solo procesamos si el usuario ha introducido un valor
            # Buscamos si ya existe un registro de stock para este producto en esa ubicación
            quant = self.env['stock.quant'].search([
                ('product_id', '=', product.id),
                ('location_id', '=', location.id)
            ], limit=1)

            if not quant:
                # Si no existe, lo creamos
                quant = self.env['stock.quant'].create({
                    'product_id': product.id,
                    'location_id': location.id,
                })
            
            # Aplicamos la nueva cantidad directamente
            quant.inventory_quantity = product.new_stock_quantity
            quant.action_apply_inventory()
            
            # Limpiamos el campo de entrada para la siguiente vez
            product.new_stock_quantity = 0.0

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }