What it does?
=============
- It is a framework for Open API for submission and verification of QRCode.
- API to check if the URL scanned is safe to visit.
- Page for collaborator to add in verified links.
  (Can be extended to serve metadata about the QRCode, helps to report malicious websites)

Source Repository at Github
===========================
https://github.com/klrkdekira/qrevent_client

QREvent source is available at
==============================
https://github.com/klrkdekira/qrevent_server

How to install
==============
$ python bootstrap

$ bin/buildout

For development

$ bin/pserve src/qrevent/development.ini

For production

$ bin/pserve src/qrevent/production.ini

How to insert default data
==========================
After running buildout

$ bin/python -m qrevent.scripts.initdb src/qrevent/[development.ini|production.ini]

Credentials created

Default username and password
=============================
username: alphadude

password: helloworld

Default API access key and private key (For HMAC)
=================================================
Not used currently

access_key: 0c36ed7f5a

private_key: 28b33a01a3680090c58923e017f4a11a

