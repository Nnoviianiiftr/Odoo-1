from odoo import models, fields

class DentalDoctor(models.Model):
    _name = 'dental.doctor'
    _description = 'Dental Doctor'

    doctor = fields.Many2one('res.partner', string="Doctor", required=True)
    image = fields.Binary(string=".", attachment=True)
    service_id = fields.Many2one('dental.service', string="Service")
    stage = fields.Selection([
        ('work', 'Work'),
        ('leave', 'Leave'),
    ], default='work', string='Status', required=True)
 
    def action_work(self):
        self.stage = 'work'
        
    def action_leave(self):
        self.stage = 'leave'
        
    list_visible = fields.Boolean(compute='_compute_list_visible', store=True)
    def _compute_list_visible(self):
        for doctor in self:
            doctor.list_visible = doctor.stage != 'leave'

    def action_work(self):
        self.stage = 'work'
        
    def action_leave(self):
        self.stage = 'leave'