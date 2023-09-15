import logging
from odoo import api, fields, models
_logger = logging.getLogger(__name__)

class MailActivity(models.Model):
    _inherit = 'mail.activity'

    date_deadline_time = fields.Datetime(string="Date Deadline Time", required=True, default=fields.Datetime.now)
    date_deadline = fields.Date(compute='_compute_date_deadline', store=True)

    @api.depends('date_deadline_time')
    def _compute_date_deadline(self):
        for rec in self:
            rec.date_deadline = rec.date_deadline_time.date()