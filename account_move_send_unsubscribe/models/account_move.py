from odoo import api, models
import logging
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        res = super(AccountMove, self).message_post(**kwargs)
        self._unsubscribe()
        return res