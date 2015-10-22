# what about saving extra variable in a QuerySet?
folder=Folder.objects.all().extra(select = {'fcount':33})
