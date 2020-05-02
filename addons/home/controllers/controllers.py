# -*- coding: utf-8 -*-
from odoo import http

# class MyModule(http.Controller):
#     @http.route('/home/home/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/home/home/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('home.listing', {
#             'root': '/home/home',
#             'objects': http.request.env['home.home'].search([]),
#         })

#     @http.route('/home/home/objects/<model("home.home"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('home.object', {
#             'object': obj
#         })