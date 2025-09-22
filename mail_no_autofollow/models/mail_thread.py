import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    @api.returns("mail.message", lambda value: value.id)
    def message_post(self, **kwargs):
        # Set the autofollow context to False
        message = super(MailThread, self.with_context(mail_post_autofollow=False)).message_post(**kwargs)
        # If current user is not author, unsubscribe the author
        if message.author_id != self.env.user.partner_id:
            self.message_unsubscribe(partner_ids=[message.author_id.id])
        return message
