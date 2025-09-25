# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MailChannelFollowers(models.Model):
    _name = "mail.channel.followers"
    _description = "Mail Channel Followers"

    channel_id = fields.Many2one("mail.channel", required=True)
    model_id = fields.Many2one("ir.model", required=True, ondelete="cascade")
    subtype_id = fields.Many2one("mail.message.subtype")
    external_only = fields.Boolean(help="Notify channel if message author is external.")
