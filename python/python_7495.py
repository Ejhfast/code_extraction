# django convert query set to array of list
myWords = MyGroup.objects.get(name = "bla").allkeyword.values_list('name', flat=True)
