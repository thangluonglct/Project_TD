# -*- coding: utf-8 -*-
from odoo import http

# class OrderReturn(http.Controller):
#     @http.route('/order_return/order_return/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/order_return/order_return/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('order_return.listing', {
#             'root': '/order_return/order_return',
#             'objects': http.request.env['order_return.order_return'].search([]),
#         })

#     @http.route('/order_return/order_return/objects/<model("order_return.order_return"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('order_return.object', {
#             'object': obj
#         })