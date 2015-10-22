# How to do aggregation with filter in django
from django.db.models import Min
models.ServerName.objects.filter(server_id=ServerName.id).aggregate(Min('time'))
