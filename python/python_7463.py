# Django script to access model objects without using manage.py shell
from your_project import settings
from django.core.management import setup_environ
setup_environ(settings)
