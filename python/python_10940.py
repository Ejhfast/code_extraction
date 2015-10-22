# Django Models - Wrong output from Many-To-Many relationship queryset?
Keyword.objects.filter(url__user__username=username1, keyword__in=Keyword.objects.filter(url__user__username=username2).values_list('keyword', flat=True)).values_list('keyword', flat=True).distinct()
