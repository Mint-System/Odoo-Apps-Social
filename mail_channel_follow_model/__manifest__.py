# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Mail Channel Follow Model",
    "summary": """
        Subscribe channels to models and receive notifications in the channel.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Repository",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mail", "sale"],
    "data": ["security/ir.model.access.csv", "views/mail_channel_views.xml"],
    "demo": ["demo/mail_channel_followers_demo.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
