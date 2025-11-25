# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MailChannel(models.Model):
    _inherit = ["discuss.channel"]

    follower_ids = fields.One2many("discuss.channel.followers", "channel_id")
