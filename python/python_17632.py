# Loading objects created by specific user in python/Django
tools = Tool.objects.filter(owner__user=request.user).order_by('name')
