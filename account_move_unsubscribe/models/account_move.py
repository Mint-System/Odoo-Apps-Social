from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _post(self, soft=True):
        res = super()._post(soft=soft)
        # Unsubscribe all followers except current user
        for am in self:
            current_partner_id = self.env.user.partner_id # am.user_invoice_id.partner_id
            am.message_subscribe([current_partner_id.id])
            message_partner_ids = am.message_partner_ids.filtered(lambda p: p != current_partner_id)
            am.message_unsubscribe(message_partner_ids.ids)
        return res