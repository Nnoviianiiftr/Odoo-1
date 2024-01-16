from odoo import models, fields

class DentalService(models.Model):
    _name = 'dental.service'
    _description = 'Dental Service'

    name = fields.Char("Name", required=True)
    floor = fields.Integer("Floor")
    room = fields.Char("Room")