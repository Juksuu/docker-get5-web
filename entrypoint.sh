#!/bin/bash

cd /var/www/get5-web
. venv/bin/activate
./manager.py db upgrade
chown -R www-data logs

source /etc/apache2/envvars
apache2 -DFOREGROUND
