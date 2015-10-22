# Basic Django query?
Teacher.objects.filter(user__id=some_id).values_list('substitute_id', flat=True)
