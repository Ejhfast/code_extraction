# How to activate/deactivate a virtualenv from python code?
activate_this = '/path/to/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
