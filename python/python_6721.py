# Django filter against Multiple Item QuerySets
EventRegistration.objects.filter(event__in=Event.objects.all())
