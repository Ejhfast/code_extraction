# How can I create an ordered dictionary from json in Python
json.loads(request.POST.get('myd'), object_pairs_hook=collections.OrderedDict)
