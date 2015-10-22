# How to get an extra count field with Django ORM?
messages = Message.objects.all()
messageReads = UserMessageRel.objects.filter(isRead=True).
    values("message_id").annotate(cnt=Count("user"))
