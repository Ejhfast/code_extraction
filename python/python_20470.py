# Aggregation with django-eztables
def get_queryset(self):
    qs = super(SomeObjectDataTableView, self).get_queryset()
    return qs.select_related().annotate(items_count=Count('items'))
