# How to Group by id and Order By count in Django
articles = ArticleTracking.objects.filter(date__range=(start_date, end_date))
articles = articles.values('story_id', 'url', 'headline').annotate(count = Count('story_id')).order_by('-count')[:20]
