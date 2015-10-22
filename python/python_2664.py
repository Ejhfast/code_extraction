# How to use OR using Django's model filter system?
from django.db.models import Q
Publisher.objects.filter(Q(name__contains="press") | Q(country__contains="U.S.A"))
