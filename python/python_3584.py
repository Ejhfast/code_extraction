# Python: extracting a list from an array of dictionaries with arrays in them
names = [child['institution_name'] for child in inst_array[0]['children']]
