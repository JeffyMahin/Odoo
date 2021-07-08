from odoo import api, fields, models, tools


class HospitalDoctor(models.Model):
    _name = "hospital_doctor.list"
    _description = "Hospital Doctor List"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    degree = fields.Char(string='Degree')