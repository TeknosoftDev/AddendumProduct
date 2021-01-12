# -*- coding: utf-8 -*-
from odoo import fields, models


class Template(models.Model):
    _inherit = 'product.template'

    addendum_ids = fields.One2many(
        comodel_name='product.template.addendum',
        string="Addendas",
        inverse_name='addendum_product_id',
    )
    