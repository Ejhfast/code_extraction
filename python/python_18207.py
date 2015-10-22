# Django orm get latest for each group
Score.objects.annotate(max_date=Max('student__score__date')).filter(date=F('max_date'))
