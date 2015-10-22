# Django Manager.values() returns a mysterious None
Test.objects.filter(date=date).exclude(color=None).values('color').distinct()
