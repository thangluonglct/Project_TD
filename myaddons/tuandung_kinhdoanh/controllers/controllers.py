# -*- coding: utf-8 -*-
from odoo import http

# class TuandungKinhdoanh(http.Controller):
#     @http.route('/tuandung_kinhdoanh/tuandung_kinhdoanh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tuandung_kinhdoanh/tuandung_kinhdoanh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tuandung_kinhdoanh.listing', {
#             'root': '/tuandung_kinhdoanh/tuandung_kinhdoanh',
#             'objects': http.request.env['tuandung_kinhdoanh.tuandung_kinhdoanh'].search([]),
#         })

#     @http.route('/tuandung_kinhdoanh/tuandung_kinhdoanh/objects/<model("tuandung_kinhdoanh.tuandung_kinhdoanh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tuandung_kinhdoanh.object', {
#             'object': obj
#         })