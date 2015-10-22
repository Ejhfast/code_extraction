# popular_events = Events.objects.annotate(attendee_count=Count('attendee')).filter(attendee_count__gt=50)
