# Convert dictionary to bytes and back again python?
s=json.dumps(variables)
variables2=json.loads(s)
assert(variables==variables2)
