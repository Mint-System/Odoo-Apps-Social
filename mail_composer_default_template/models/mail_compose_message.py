from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.model
    def get_record_data(self, values):
        """
        Set default template in the following priority:
        1. Template id given in values
        2. First assigned template with valid domain
        3. First assigned template
        4. None
        """

        res = super().get_record_data(values)
        _logger.warning([res,values])

        template_ids = self.env['mail.template'].search([('model', '=', values.get('model'))])
        ressource_id = self.env[values['model']].browse(values.get('res_id'))
        domain_template_ids = []

        for template in template_ids:
            domain = eval(template.domain)
            if domain and ressource_id.filtered_domain(domain):
                domain_template_ids.append(template)

        if values.get('template_id', 0) != 0:
            return res
        elif domain_template_ids:
            res['template_id'] = domain_template_ids[0].id
        elif template_ids:
            res['template_id'] = template_ids[0].id
        else:
            res['template_id'] = ''
        
        return res
