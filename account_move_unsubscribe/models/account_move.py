from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _post(self, soft=True):
        res = super()._post(soft=soft)
        # Unsubscribe all followers except invoice user
        for am in self:
            message_partner_ids = am.message_partner_ids.filtered(lambda p: p != am.invoice_user_id.partner_id)
            am.message_unsubscribe(message_partner_ids.ids)
        return res