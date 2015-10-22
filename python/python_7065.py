# django make query
target_filter = 'Class'
search_result = AAA.objects.filter(**{target_filter:3}).count()
