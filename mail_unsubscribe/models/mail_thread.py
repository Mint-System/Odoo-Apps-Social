from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)
import ast


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _unsubscribe_followers(self):
        ignore_current_partner = ast.literal_eval(self.env['ir.config_parameter'].sudo().get_param('mail_unsubscribe.ignore_current_partner', 'False'))
        for mt in self:
            current_partner_id = self.env.user.partner_id
            message_partner_ids = mt.message_partner_ids
            if ignore_current_partner:
                message_partner_ids = message_partner_ids.filtered(lambda p: p != current_partner_id)
            _logger.warning(['message_unsubscribe', mt, message_partner_ids])
            mt.message_unsubscribe(message_partner_ids.ids)


    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        self._unsubscribe_followers()
        mail_post_autofollow = ast.literal_eval(self.env['ir.config_parameter'].sudo().get_param('mail_unsubscribe.mail_post_autofollow', 'False'))
        mail_create_nosubscribe = ast.literal_eval(self.env['ir.config_parameter'].sudo().get_param('mail_unsubscribe.mail_create_nosubscribe', 'True'))
        res = super(MailThread, self.with_context(mail_post_autofollow=mail_post_autofollow, mail_create_nosubscribe=mail_create_nosubscribe)).message_post(**kwargs)
        return res