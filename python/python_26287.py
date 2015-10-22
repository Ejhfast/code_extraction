# Is there a one-liner for removing whitespace and specific characters?
bad_symbols = '(){}\n'
s = 'hello () { world \n }'
s = ''.join([x for x in s if x not in bad_symbols])
