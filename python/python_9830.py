# How to get string on .values() to foreign key?
JobPost.objects.filter(production=p).values('position__position')
