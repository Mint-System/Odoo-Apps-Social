from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)
import ast


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _unsubscribe(self):
        unfollow_all = ast.literal_eval(self.env["ir.config_parameter"].sudo().get_param("mail.unsubscribe_all", "False"))
        for am in self:
            current_partner_id = self.env.user.partner_id # am.user_invoice_id.partner_id
            am.message_subscribe([current_partner_id.id])
            message_partner_ids = am.message_partner_ids
            if not unfollow_all:
                message_partner_ids = message_partner_ids.filtered(lambda p: p != current_partner_id)
            am.message_unsubscribe(message_partner_ids.ids)

    def _post(self, soft=True):
        """Unsubscribe all followers except current user."""
        res = super()._post(soft=soft)
        self._unsubscribe()
        return res
