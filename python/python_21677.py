# Can't bind many to many field correctly
note = Note.objects.get(id=1)
note.tags.all()
