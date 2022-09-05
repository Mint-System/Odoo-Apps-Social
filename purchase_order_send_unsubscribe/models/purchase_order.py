from odoo import api, models
import logging
_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        res = super(PurchaseOrder, self).message_post(**kwargs)
        self._unsubscribe()
        return res