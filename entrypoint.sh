#!/bin/bash

cd /var/www/get5-web
. venv/bin/activate
./manager.py db upgrade
chown -R www-data logs

rm -f /var/run/apache2/apache2.pid

source /etc/apache2/envvars
apache2 -DFOREGROUND
