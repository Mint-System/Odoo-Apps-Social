import logging

from odoo import api, models
from odoo.tools.safe_eval import safe_eval

_logger = logging.getLogger(__name__)


class MailComposeMessage(models.TransientModel):
    _inherit = "mail.compose.message"

    @api.model
    def default_get(self, fields_list):
        """
        Set default template in the following priority:
        1. Template id given in values
        2. First assigned template with valid domain
        3. First assigned template
        4. None
        """
        res = super().default_get(fields_list)

        # if 'template_id' not in fields_list or res.get('template_id'):
        #     return res

        model = res.get("model")
        if not model:
            return res

        res_ids_raw = res.get("res_ids")
        res_id = False
        if res_ids_raw:
            ids = safe_eval(res_ids_raw) if isinstance(res_ids_raw, str) else res_ids_raw
            res_id = ids[0] if ids else False

        if not res_id:
            return res

        templates = self.env["mail.template"].search([("model", "=", model)])
        if not templates:
            return res

        ressource_id = self.env[model].browse(res_id)
        domain_templates = templates.filtered(lambda t: t.domain and ressource_id.filtered_domain(safe_eval(t.domain)))
        res["template_id"] = (domain_templates or templates)[0].id
        return res
