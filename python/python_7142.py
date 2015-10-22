# Marking query in particular case
Question.objects.filter(answer__isnull=False).distinct()
