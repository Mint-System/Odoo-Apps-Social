# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import models

_logger = logging.getLogger(__name__)


class MailMessage(models.Model):
    _inherit = "mail.message"

    def _message_fetch(self, domain, search_term=None, before=None, after=None, around=None, limit=30):
        result = super()._message_fetch(domain, search_term, before, after, around, limit)

        result["messages"] = result["messages"].sorted("date", reverse=True)

        return result
