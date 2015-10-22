# view permission if request data not in queryset
filename = self.request.GET.get('filename')
if FileIndex.objects.filter(filename=filename).exists():
    #do something
