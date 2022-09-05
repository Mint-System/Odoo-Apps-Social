from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)
import ast


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _unsubscribe(self):
        unfollow_all = ast.literal_eval(self.env["ir.config_parameter"].sudo().get_param("mail.unsubscribe_all", "False"))
        for po in self:
            message_partner_ids = po.message_partner_ids
            if not unfollow_all:
                message_partner_ids = message_partner_ids.filtered(lambda p: p != po.user_id.partner_id)
            po.message_unsubscribe(message_partner_ids.ids)

    def button_confirm(self):
        """Unsubscribe all followers except purchase user."""
        res = super().button_confirm()
        self._unsubscribe()
        return res