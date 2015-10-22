# How do I get queryset containing all referenced objects with a specific user field?
ContactDetails.objects.filter(server__user=request.user)
