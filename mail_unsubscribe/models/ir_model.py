from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class IrModel(models.Model):
    _inherit = 'ir.model'

    unsubscribe_before_message_post = fields.Boolean(default=True, help="Remove all subscribers before message post.")