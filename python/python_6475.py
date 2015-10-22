# Make filters of an object list
from django.db.models import Q
Advertisement.objects.filter( Q(name = 'Paris') | Q(name = 'New York') )
