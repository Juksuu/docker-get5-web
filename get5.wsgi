#!/usr/bin/python

activate_this = '/var/www/get5-web/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)

folder = "/var/www/get5-web"
if not folder in sys.path:
    sys.path.insert(0, folder)
sys.path.insert(0,"")

from get5 import app as application
import get5
get5.register_blueprints()
