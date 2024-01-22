from odoo import models, fields

class DentalPatient(models.Model):
    _name = 'dental.patient'
    _description = 'Dental Patient'
    

    patient = fields.Many2one('res.partner', string="Patient", required=True)
    image = fields.Binary(string="image", attachment=True)
    doctor = fields.Many2one('res.partner', string="Doctor")
    service = fields.Many2one('dental.service', string="Service")
    emergency_number = fields.Char("Emergency Number", related='patient.phone')
    date_of_birth = fields.Date("Date of Birth")
    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ], string="Blood Type")
    height = fields.Float("Height")
    weight = fields.Float("Weight")
    is_vaccinated = fields.Boolean("Is Vaccinated")
    vaccine_name = fields.Char("Vaccine Name")
    stage = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], default='new', string='Stage', required=True)

    def action_new(self):
        self.stage = 'new'

    def action_in_progress(self):
        self.stage = 'in_progress'

    def action_done(self):
        self.stage = 'done'