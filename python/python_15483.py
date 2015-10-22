# Empty values retrieved with values_list
from django.db.models import Q
list_countries = Country.objects.filter(~Q(country_name='')).values_list('country_name', flat=True).distinct()
