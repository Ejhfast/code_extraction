# When using the Django model library, what is the syntax for creating "or" statements in filters?
from django.db.models import Q
SomeModel.objects.filter(Q(propertyA=foo) | Q(propertyB=bar))
