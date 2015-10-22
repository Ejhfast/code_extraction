# Django: queryset multiple conditions or gather into new object
query = Comment.objects.filter(project__user=person)
