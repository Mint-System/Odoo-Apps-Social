from odoo import models,api
import logging
_logger = logging.getLogger(__name__)


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    """
     - `mail_create_nosubscribe`: at create or message_post, do not subscribe
       uid to the record thread
     - `mail_create_nolog`: at create, do not log the automatic '<Document>
       created' message
     - `mail_notrack`: at create and write, do not perform the value tracking
       creating messages
     - `tracking_disable`: at create and write, perform no MailThread features
       (auto subscription, tracking, post, ...)
     - `mail_notify_force_send`: if less than 50 email notifications to send,
       send them directly instead of using the queue; True by default
     - `mail_post_autofollow`: Automatically subscribe recipients if asked to
    """

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        return super(MailThread, self.with_context(mail_post_autofollow=False)).message_post(**kwargs)
