# Reaching a dictionary inside a list of dictionaries by key
first_with_id_or_none = \
    next((value for value in dictionary['items'] if value['id'] == 1), None)
