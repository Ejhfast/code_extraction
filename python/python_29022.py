# Annotate many to many relation in Django
VideoData.objects.annotate(
        watches_count=models.Count('user_set')
    ).order_by('-watches_count')[:10]
