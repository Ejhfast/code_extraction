# Python: how to sort array of dicts by two fields?
ws.sort(key=lambda datum: (datum['date'], datum['type'], datum['location']))
