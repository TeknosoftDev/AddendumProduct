from odoo import fields, models


class Accountmove(models.Model):
    _inherit = 'account.move.line'

    additional_data = fields.Char(
    )
    