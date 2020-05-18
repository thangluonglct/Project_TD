
from odoo import models, fields, api

class tuandung_kinhdoanh(models.Model):
    # _inherit = 'sale.order'
    _name = 'tuandung.kinhdoanh'
    dat_tour = fields.Boolean(string="Đặt Tour")
    ten = fields.Char(string="Tên")