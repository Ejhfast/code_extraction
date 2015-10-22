# Python create dict from other dict
keys = ['name', 'last_name', 'phone_number', 'email']
dict1 = {x:dict1[x] for x in keys}
