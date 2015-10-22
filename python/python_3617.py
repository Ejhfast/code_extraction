# Update model django through kwargs
obj = Object(index=id, **fields)
obj.save()
