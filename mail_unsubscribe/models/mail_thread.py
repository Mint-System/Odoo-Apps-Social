import ast
import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def _unsubscribe_followers(self):
        ignore_current_partner = ast.literal_eval(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("mail_unsubscribe.ignore_current_partner", "False")
        )
        current_partner_id = (
            self.env.user.partner_id
        )  # Defined outside the loop for scope clarity
        for rec in self:
            message_partner_ids = rec.message_partner_ids
            if ignore_current_partner:
                message_partner_ids = message_partner_ids.filtered(
                    lambda p: p != current_partner_id
                )
            rec.message_unsubscribe(message_partner_ids.ids)

    @api.returns("mail.message", lambda value: value.id)
    def message_post(self, **kwargs):
        mail_post_autofollow = ast.literal_eval(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("mail_unsubscribe.mail_post_autofollow", "False")
        )
        mail_create_nosubscribe = ast.literal_eval(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("mail_unsubscribe.mail_create_nosubscribe", "False")
        )

        if self._name != "discuss.channel":
            self._unsubscribe_followers()
            self = self.with_context(
                mail_post_autofollow=mail_post_autofollow,
                mail_create_nosubscribe=mail_create_nosubscribe,
            )
            return super().message_post(**kwargs)
        else:
            return super().message_post(**kwargs)
