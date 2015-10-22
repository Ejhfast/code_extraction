# Grab header variable in Python
from flask import request
country_code = request.environ.get('GEOIP_COUNTRY_CODE')
