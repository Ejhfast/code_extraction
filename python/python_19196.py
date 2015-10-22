# Django model latest() method
rule = Rule.objects.filter(user=user).latest('id')
