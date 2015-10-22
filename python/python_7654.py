# Django query foreign object that occurs more than once
from django.db.models import Count
Checkins.objects.filter(user=my_user).annotate(chkn_count=Count('location')).order_by('-chkn_count')
