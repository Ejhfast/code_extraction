# Load fixture.json through python script
from django.core.management import call_command
call_command('loaddata', 'data.json', stdout=out, verbosity=0)
