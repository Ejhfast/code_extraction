# bulk_create how to call function on each object
for obj in objs:
    obj.send(gateway)
Message.objects.bulk_create(objs)
