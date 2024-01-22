from odoo import models, fields

class DentalAppointment(models.Model):
    _name = 'dental.appointment'
    _description = 'Dental Appointment'

    patient = fields.Many2one('res.partner', string="Patient", required=True)
    image = fields.Binary(string="image", attachment=True)
    doctor = fields.Many2one('res.partner', string="Doctor", required=True)
    service = fields.Many2one('dental.service', string="Service", required=True)
    date_start = fields.Datetime("Start Date")
    date_end = fields.Datetime("End Date")
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