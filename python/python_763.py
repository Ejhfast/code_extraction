# Making tabulation look different than just whitespace
User in Form-Class
self.fields['myfield'].choices = [('%s' % d.id, '%s' % d.name) for d in MyModel.objects.filter(owners = user)]
