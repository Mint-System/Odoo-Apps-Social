import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model_create_multi
    def create(self, vals_list):
        _logger.warning("create called")
        return super(
            AccountMove, self.with_context(tracking_disable=True)
        ).create(vals_list)

    def write(self, vals):
        _logger.warning("write called")

        return super(
            AccountMove, self.with_context(tracking_disable=True)
        ).write(vals)

    def message_post(self, **kwargs):
        if self.env.context.get("tracking_disable"):
            return self.env["mail.message"]
        return super().message_post(**kwargs)