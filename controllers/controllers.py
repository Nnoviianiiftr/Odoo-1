# -*- coding: utf-8 -*-
# from odoo import http


# class DentalCare(http.Controller):
#     @http.route('/dental__care/dental__care', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dental__care/dental__care/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dental__care.listing', {
#             'root': '/dental__care/dental__care',
#             'objects': http.request.env['dental__care.dental__care'].search([]),
#         })

#     @http.route('/dental__care/dental__care/objects/<model("dental__care.dental__care"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dental__care.object', {
#             'object': obj
#         })

