# How can I refactor this django query to not select each individual object?
attendees = rsvp.attendee_set.select_related().all().order_by('email__first_name')
