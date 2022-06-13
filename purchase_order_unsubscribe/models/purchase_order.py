from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def button_confirm(self):
        res = super().button_confirm()
        # Unsubscribe all followers except purchase user
        for po in self:
            message_partner_ids = po.message_partner_ids.filtered(lambda p: p != po.user_id.partner_id)
            po.message_unsubscribe(message_partner_ids.ids)
        return res