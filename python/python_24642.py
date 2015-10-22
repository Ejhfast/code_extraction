# Tricky Django QuerySet with Complicated ForeignKey Traversals
return BuildPart.objects.filter(build__id=part.product.pk)
