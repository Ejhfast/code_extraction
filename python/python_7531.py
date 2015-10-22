# Django QuerySet with exclude & annotate not returning any results
types_qs.annotate(num_components=Count('components')).filter(Q(is_bulk=False) | (Q(is_bulk=True) &amp; Q(num_components__gt=0)))
