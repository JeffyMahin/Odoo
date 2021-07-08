from odoo import api, fields, models, tools, _


class HospitalPatient(models.Model):
    _name = "hospital_patient.list"
    _description = "Hospital Patient List"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    doctor_id = fields.Many2one('hospital_doctor.list', string='Doctor')
    patient_type = fields.Char(string='Patient Type')
    reference = fields.Char(string='Reference', required=True, copy=False,
                           readonly=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('hospital_patient_seq_code')
        if vals.get('reference', _('New'))== _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital_patient_seq_code') or _('New')

        # age = vals.get('age')
        # if age>=50:
        #     vals['patient_type']= 'Serious'
        #
        # if age>=90:
        #     vals['patient_type']= 'Super Serious'


        print("Successfully overrided create method")
        return super(HospitalPatient, self).create(vals)
