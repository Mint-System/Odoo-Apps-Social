import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    ignore_current_partner = fields.Boolean(
        config_parameter="mail_unsubscribe.ignore_current_partner"
    )
    mail_post_autofollow = fields.Boolean(
        config_parameter="mail_unsubscribe.mail_post_autofollow"
    )
    mail_create_nosubscribe = fields.Boolean(
        config_parameter="mail_unsubscribe.mail_create_nosubscribe"
    )
