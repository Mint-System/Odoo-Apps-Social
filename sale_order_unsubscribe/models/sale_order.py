from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super().action_confirm()
        # Unsubscribe all followers
        for so in self:
            so.message_unsubscribe(so.message_partner_ids.ids)
        return res