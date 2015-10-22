# Running Python from a virtualenv with Apache/mod_wsgi, on Windows
activate_this = '/path/to/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
