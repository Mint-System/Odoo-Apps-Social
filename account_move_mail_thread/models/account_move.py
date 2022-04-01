from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model_create_multi
    def create(self, vals_list):
        _logger.warning('Call create method with tracking disabled.')
        return super(AccountMove, self.with_context(tracking_disable=True)).create(vals_list)
    
    def message_post_with_view(self, views_or_xmlid, **kwargs):
        _logger.warning('Do not call message post with view method.')
        return