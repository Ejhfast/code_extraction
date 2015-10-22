# How to delete a value from 'ValuesListQuerySet' in django?
User.objects.exclude(pk__in=Device.objects.values_list('user', flat=True).distinct())
