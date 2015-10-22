# why 1 is ok,but 2 is error,use django and jquery
from django.test.client import Client
c = Client()
response = c.get('/json_view/', {'tag': 'email', 'email': '...'})
