# wrong Python version when using Virtualenv in pythonanywhere
rmvirtualenv django18
mkvirtualenv --python=/usr/bin/python3.3 django18
pip install django # reinstall django and any other packages you need.
