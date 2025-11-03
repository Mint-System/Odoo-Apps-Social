Setup:

- Setup discussion channel and subscribe to sale.order model
- Set subtype to "Discussion" and enable "external only"

Portal user:

- Setup portal account for gemini.furniture39@example.com
- Login with portal account in private browser tab
- Send a message as portal user to S00007
- Check if message in sale channel

Odoo bot:

- Install sale_subscrption
- Open S00022
- Set start date minus 1 year
- Set next invoice date minus 1 month
- Open subscription phase "closed" and set mail template "Abonnement: Bewertungsanfrage"
- Run server action "Ablauf des Abonnements"
- Ensure there is no message by Odoo bot
