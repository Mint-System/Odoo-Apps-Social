from odoo import api, models
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        res = super(SaleOrder, self).message_post(**kwargs)
        self._unsubscribe()
        return res