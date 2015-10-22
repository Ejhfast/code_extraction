# Django: Getting complement of queryset
qs = Model.objects.filter(...) # qs with objects to exclude
result = Model.objects.exclude(pk__in=qs.values_list('pk', flat=True))
