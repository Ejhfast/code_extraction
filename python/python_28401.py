# Split by regex without resulting empty strings in Python
results = re.split(...)
results = list(filter(None, results))
