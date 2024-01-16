from odoo import models, fields

class DentalAppointment(models.Model):
    _name = 'dental.appointment'
    _description = 'Dental Appointment'

    patient = fields.Many2one('res.partner', string="Patient", required=True)
    doctor = fields.Many2one('res.partner', string="Doctor", required=True)
    service = fields.Many2one('dental.service', string="Service", required=True)
    date_start = fields.Datetime("Start Date")
    date_end = fields.Datetime("End Date")
