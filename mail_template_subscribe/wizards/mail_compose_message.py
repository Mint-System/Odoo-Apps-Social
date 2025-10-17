import logging

from odoo import models
from odoo.tools.safe_eval import safe_eval

_logger = logging.getLogger(__name__)


class MailComposeMessage(models.TransientModel):
    _inherit = "mail.compose.message"

    def _action_send_mail(self, auto_commit=False):
        """Add subscribers as followers to mail object."""
        for mail in self:
            if mail.template_id:
                res_ids = safe_eval(mail.res_ids)
                records = self.env[mail.model].browse(res_ids)
                subscriber_ids = mail.template_id.get_subscriber_ids()
                if subscriber_ids:
                    records._message_subscribe(partner_ids=subscriber_ids.ids)
        return super()._action_send_mail(auto_commit)
