# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, models

_logger = logging.getLogger(__name__)


class MailThread(
    models.AbstractModel,
):
    _inherit = ["mail.thread"]

    def _notify_thread(self, message, msg_vals=False, **kwargs):
        """
        Notify subscribed channels.
        """
        recipients_data = super()._notify_thread(message, msg_vals=msg_vals, **kwargs)
        if message.model and message.res_id:
            model_id = self.env["ir.model"]._get(message.model)
            if model_id and model_id.follower_ids:
                record = self.env[message.model].browse(message.res_id)
                if record:
                    record_name = record.display_name
                    record_url = "/web#id=%s&model=%s&view_type=form" % (message.res_id, message.model)
                    link = '<a href="%s" target="_blank">%s</a>' % (record_url, record_name)
                    body = _("There is a new message on %s", link)
                    for follower_id in model_id.follower_ids:
                        follower_id.channel_id.message_post(
                            body=body,
                            message_type="comment",
                        )
        return recipients_data
