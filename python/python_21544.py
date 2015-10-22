# How to filter records from a model within view?
polls_list = Event.objects.filter(inserttime__gt=timezone.now()).order_by('-inserttime')
