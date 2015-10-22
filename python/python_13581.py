# Extending get_object_or_404 to use select_related
sample = get_object_or_404(models.Sample.objects.select_related(), **kwargs)
