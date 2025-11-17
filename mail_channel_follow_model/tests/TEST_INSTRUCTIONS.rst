Setup:

- Install sale_management and contacts
- Login as admin
- Subscribe to "sales" channel

Portal user:

- Setup portal account for gemini.furniture39@example.com
- Login with portal account in private browser tab
- Send a message "ping" as portal user to S00007
- As admin if message is in "sales" channel

Odoo bot:

- Create a server action "Send message" for "sale.order"

```python
sale_order = env['sale.order'].search([('name', '=', 'S00007')])
sale_order.message_post(body="ping", partner_ids=[env.ref('base.partner_admin').id], subtype_xmlid='mail.mt_comment')
```

- Execute the action
- Ensure there is no message by Odoo bot
- Open the follow settings of the channel and disable the "external only" option
- Execute the action again
- Check if message is in "sales" channel
