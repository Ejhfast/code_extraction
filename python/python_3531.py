# Handling lazy JSON in Python - 'Expecting property name'
j = re.sub(r"{\s*(\w)", r'{"\1', j)
j = re.sub(r",\s*(\w)", r',"\1', j)
j = re.sub(r"(\w):", r'\1":', j)
