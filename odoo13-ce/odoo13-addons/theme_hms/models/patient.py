from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hms.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('mane', 'Male'),
        ('femal', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')