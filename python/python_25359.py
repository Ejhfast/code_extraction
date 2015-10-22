# Django order query by foreign key (reverse direction)
from django.db.models import Max
objs = Obj.objects.annotate(latest_data=Max('objdata__datum')).order_by('latest_data')
