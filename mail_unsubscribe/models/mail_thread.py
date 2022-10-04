from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)
import ast


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _unsubscribe_followers(self):
        ignore_current_partner = ast.literal_eval(self.env['ir.config_parameter'].sudo().get_param('mail_unsubscribe.ignore_current_partner', 'False'))
        for am in self:
            current_partner_id = self.env.user.partner_id # am.user_invoice_id.partner_id
            message_partner_ids = am.message_partner_ids
            if ignore_current_partner:
                message_partner_ids = message_partner_ids.filtered(lambda p: p != current_partner_id)
            am.message_unsubscribe(message_partner_ids.ids)


    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        self._unsubscribe_followers()
        res = super(self.with_context(mail_post_autofollow=False)).message_post(**kwargs)
        return res