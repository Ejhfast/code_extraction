# split a string by a delimiter in a context sensitive way
re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', str)
