# Check if object with OneToOneField is new or already exists
new  =  not bool(X.objects.filter(pk=self.pk).count())
