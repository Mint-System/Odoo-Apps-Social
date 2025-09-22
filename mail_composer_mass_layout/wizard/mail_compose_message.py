import logging

from odoo import models

_logger = logging.getLogger(__name__)


class MailComposer(models.TransientModel):
    _inherit = "mail.compose.message"

    def render_message(self, res_ids):
        """
        This method returns the email values including the mail body.
        It iterates on the records and updates the mail body with the layout.
        """
        template_values = super().render_message(res_ids)

        for res_id in res_ids:
            template_value = template_values[res_id]

            # Get record and model
            record = self.env[self.model].browse(res_id)
            model = self.env["ir.model"]._get(record._name)

            # Prepare template
            template_ctx = {
                "message": self.env["mail.message"]
                .sudo()
                .new(dict(body=template_value["body"], record_name=record.display_name)),
                "model_description": model.display_name,
                "company": "company_id" in record and record["company_id"] or self.env.company,
            }

            # Render template with layout
            body = model.env["ir.qweb"]._render(
                self.env.ref("mail.mail_notification_light").id,
                template_ctx,
                minimal_qcontext=True,
            )

            # Update with new body
            template_values[res_id]["body"] = body

        return template_values
