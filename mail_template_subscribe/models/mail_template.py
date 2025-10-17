import logging

from odoo import fields, models
from odoo.tools.safe_eval import safe_eval

_logger = logging.getLogger(__name__)


class MailTemplate(models.Model):
    _inherit = "mail.template"

    subscriber_domain = fields.Char(
        required=True,
        default="[('id', '=', user.partner_id.id)]",
        help="Contacts machting this domain will be subscribed to the mail document.",
    )

    def get_subscriber_ids(self):
        eval_context = {
            "user": self.env.user,
        }
        domain = safe_eval(self.subscriber_domain, eval_context)
        return self.env["res.partner"].search(domain)
