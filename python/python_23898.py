# Django 1.7 - Accidentally Dropped One Table. How To Recover It?
python manage.py sqlmigrate app_name 0001 | python manage.py dbshell
