from odoo.odoo import models, fields


class Person(models.Model):
    _name = 'test.person'
    _description = 'Person Model'

    name = fields.Char(size= 32, string='Person Name')
    address = fields.Char(size= 100, string='Address')