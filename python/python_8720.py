# iterating over related objects in django
for contact in participant.person.mailcontact_set.all():
