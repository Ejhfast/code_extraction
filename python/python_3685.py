# Python: create a list of dictionaries using a list comprehension
entries_expanded[:] = [{'id':entry['id'], 'supplier':myfunction(entry['supplier'])} for entry in entries_expanded]
