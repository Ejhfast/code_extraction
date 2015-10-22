# How to extract value with simplejson?
jstr = json.loads(my_string)
if jstr.get('response'):
    jstr_response = jstr.get('response')[1][0].get('name')
