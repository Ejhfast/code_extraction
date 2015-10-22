# Django: select all A objects that are involved in m2m relationships with any B objects (via B.m2mfield)
People.objects.exclude(recordings=None)
