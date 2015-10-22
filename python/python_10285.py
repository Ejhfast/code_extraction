# Table x has no column y even after app has been reset
python manage.py sqlclear appname
python manage.py syncdb
