# how do I sort a python list of dictionaries given a list of ids with the desired order?
users.sort(key=lambda x: order.index(x['id']))
