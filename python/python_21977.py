# Filtering on foreign keys
def get_queryset(self):
    return Article.objects.filter(foreignkey__valuefield=self.kwargs['value'])
