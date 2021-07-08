# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TestPerson(models.Model):
    _name = 'test.person'
    _description = 'test_person.test_person'

    name = fields.Char()
    address = fields.Text()

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
