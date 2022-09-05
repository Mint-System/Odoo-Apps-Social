from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)
import ast


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _unsubscribe(self):
        unfollow_all = ast.literal_eval(self.env["ir.config_parameter"].sudo().get_param("mail.unsubscribe_all", "False"))
        for so in self:
            message_partner_ids = so.message_partner_ids
            if not unfollow_all:
                message_partner_ids = so.message_partner_ids.filtered(lambda p: p != so.user_id.partner_id)
            so.message_unsubscribe(message_partner_ids.ids)

    def action_confirm(self):
        """Unsubscribe all followers except sales person."""
        res = super().action_confirm()
        self._unsubscribe()
        return res