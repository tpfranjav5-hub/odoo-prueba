from odoo import models, fields, api

class ProductTemplateAttributeLine(models.Model):
    _inherit = 'product.template.attribute.line'

    allow_multiple_selection = fields.Boolean(string="Selección Múltiple")
    selection_limit = fields.Integer(string="Límite Máximo", default=1)

    # Enviamos los datos al TPV
    @api.model
    def _load_pos_data_fields(self, config_id):
        fields = super()._load_pos_data_fields(config_id)
        fields += ['allow_multiple_selection', 'selection_limit']
        return fields