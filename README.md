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

