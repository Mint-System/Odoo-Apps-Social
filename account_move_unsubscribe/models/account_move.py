from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _post(self, soft=True):
        res = super()._post(soft=soft)
        # Unsubscribe all followers
        for am in self:
            am.message_unsubscribe(am.message_partner_ids.ids)
        return res