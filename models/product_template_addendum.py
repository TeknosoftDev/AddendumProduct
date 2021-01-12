# -*- coding: utf-8 -*-
from datetime import timedelta


from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProductTemplateAddendum(models.Model):
    _name = 'product.template.addendum'
    _description = 'Product Template Addenda'

    codeEAN = fields.Char(
    )

    codeSKU = fields.Char(        
    )

    language = fields.Selection(
        [ ('ESP', 'Español'),('ENG', 'Inglés'),],'Type', default='ESP'
    )

    addendum_product_id = fields.Many2one(
        comodel_name='product.template',
        ondelete='cascade',
        required=True,
    )

    addendum_id = fields.Many2one(
        comodel_name='account.move.addendum',
        required=True,
    )

    name = fields.Char(
    )

    codInt = fields.Char(
    )

    codExt = fields.Char(
    )

    codeCoppel = fields.Char(
    )

    @api.onchange('addendum_id')
    def _change_name(self):
        for record in self:
            record.name = record.addendum_id.name

    
    
    
