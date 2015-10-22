# A python script that activates the virtualenv and then runs another python script?
@echo off
cmd /k "cd /d C:\Users\Admin\Desktop\venv\Scripts &amp; activate &amp; cd /d    C:\Users\Admin\Desktop\helloworld &amp; python manage.py runserver"
