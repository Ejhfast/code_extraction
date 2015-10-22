# is it possible to query with a logical OR in django
from django.db import models
Organization.objects.filter(models.Q(members=me) | models.Q(founder=me))
