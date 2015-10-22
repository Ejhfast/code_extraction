# Django: Check if a object exists but isn't current instance of object
pg = Page.objects.filter(order=data).exclude(pk=self.instance.pk)
