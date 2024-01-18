from odoo import models, fields

class DentalDoctor(models.Model):
    _name = 'dental.doctor'
    _description = 'Dental Doctor'

    doctor = fields.Many2one('res.partner', string="Doctor", required=True)
    image = fields.Binary(string="image", attachment=True)
    service_id = fields.Many2one('dental.service', string="Service")