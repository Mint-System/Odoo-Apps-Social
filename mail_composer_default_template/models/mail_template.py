from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class MailTemplate(models.Model):
    _inherit = 'mail.template'
    _order = 'sequence'

    domain = fields.Text(default='[]')
    sequence = fields.Integer()