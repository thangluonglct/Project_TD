# -*- coding: utf-8 -*-

from odoo import models, fields, api

class order_return(models.Model):
    _inherit = 'sale.order'

    don_tra_hang = fields.Boolean(string="Là đơn trả hàng")
    sale_order = fields.Many2one('sale.order',domain="[('partner_id','=',partner_id),('state','=','sale')]")

    ly_do = fields.Many2one('order.new', string="Lý do")
    state_return = fields.Selection([
        ('draft', 'Draft'),
        ('order_return', 'Order Return')],default='draft',string='Status')
    kho_luutru = fields.Selection([('kho_binh_thuong','Kho bình thường'),('kho_hu_hong','Kho hư hỏng')], string="Kho lưu trữ")
    thoigian_th = fields.Date(string="Thời gian trả hàng")

    @api.multi
    def order_return(self):
        self.state_return = 'order_return'

    @api.onchange('sale_order')
    def change_id(self):
        data = []
        for line in self.sale_order.order_line:
            data.append((0, 0, {
                'product_id': line.product_id,
                'price_unit': line.price_unit,
                'product_uom': line.product_uom,
                'name': line.name,
            }))

        self.order_line = data

class order_new(models.Model):
    _name = 'order.new'

    name =fields.Char()
