# Celeryd running multiple daemons
root     24806  0.1  1.8  51404 31328 ?        Sl   Oct19   9:25 ../../.env/bin/python manage.py celeryd -f /var/log/myapp/celeryd.log -l WARNING --pidfile /var/run/celeryd.pid -B --scheduler djcelery.schedulers.DatabaseScheduler
root     24900  0.1  1.6  51404 28592 ?        S    Oct19   6:02 ../../.env/bin/python manage.py celeryd -f /var/log/myapp/celeryd.log -l WARNING --pidfile /var/run/celeryd.pid -B --scheduler djcelery.schedulers.DatabaseScheduler
root     24901  0.3  9.4 183232 161948 ?       S    Oct19  22:32 ../../.env/bin/python manage.py celeryd -f /var/log/myapp/celeryd.log -l WARNING --pidfile /var/run/celeryd.pid -B --scheduler djcelery.schedulers.DatabaseScheduler
