from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def button_confirm(self):
        res = super().button_confirm()
        # Unsubscribe all followers
        for po in self:
            po.message_unsubscribe(po.message_partner_ids.ids)
        return res