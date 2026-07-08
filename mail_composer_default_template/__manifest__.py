{
    "name": "Mail Composer Default Template",
    "summary": """
        Set default mail template for the mail composer.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch",
    "category": "Tools",
    "version": "15.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mail"],
    "data": ["views/mail.xml"],
    "qweb": ["static/src/xml/board.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
