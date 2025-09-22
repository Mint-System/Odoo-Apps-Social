# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class IrModel(models.Model):
    _inherit = ["ir.model"]

    follower_ids = fields.One2many("mail.channel.followers", "model_id")
