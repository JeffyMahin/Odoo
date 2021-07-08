# -*- coding: utf-8 -*-
# from odoo import http


# class TestPerson(http.Controller):
#     @http.route('/test_person/test_person/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_person/test_person/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_person.listing', {
#             'root': '/test_person/test_person',
#             'objects': http.request.env['test_person.test_person'].search([]),
#         })

#     @http.route('/test_person/test_person/objects/<model("test_person.test_person"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_person.object', {
#             'object': obj
#         })
