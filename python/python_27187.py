# django-haystack elasticsearch multiple indexes wrong results
sqs = SearchQuerySet().filter_or(content__contains=q).filter_or(employees__name__contains=q).filter_or(projects_name__contains=q)
# etc.
