from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super().action_confirm()
        # Unsubscribe all followers except sales person
        for so in self:
            message_partner_ids = so.message_partner_ids.filtered(lambda p: p != so.user_id.partner_id)
            so.message_unsubscribe(message_partner_ids.ids)
        return res