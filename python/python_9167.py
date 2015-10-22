# filtering only n elements in django model
qs = ModelName.object.filter(param=param).order_by('-created')[:2]
