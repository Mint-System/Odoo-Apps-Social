from odoo import models,api
import logging
_logger = logging.getLogger(__name__)


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    """
     - ``mail_create_nosubscribe``: at create or message_post, do not subscribe
       uid to the record thread
     - ``mail_create_nolog``: at create, do not log the automatic '<Document>
       created' message
     - ``mail_notrack``: at create and write, do not perform the value tracking
       creating messages
     - ``tracking_disable``: at create and write, perform no MailThread features
       (auto subscription, tracking, post, ...)
     - ``mail_notify_force_send``: if less than 50 email notifications to send,
       send them directly instead of using the queue; True by default
     - ``mail_post_autofollow``: Automatically subscribe recipients if asked to
    """

    @api.model_create_multi
    def create(self, vals_list):
        return super(MailThread, self.with_context(mail_create_nosubscribe=True)).create(vals_list)

    def write(self, values):
        return super(MailThread, self.with_context(mail_notrack=True)).write(values)
 
    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        # _logger.warning(self._context.get('mail_create_nosubscribe'))
        return super(MailThread, self.with_context(mail_create_nosubscribe=True, mail_post_autofollow=False)).message_post(**kwargs)
