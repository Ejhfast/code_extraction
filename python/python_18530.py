# How can I count the number of elements given to a column sum from a list of dictionaries quickly?
tally = {k: sum(d.get(k) if k != 'count' else 1 for d in data if d.get('code') == code and d.get('type') == type and d.get('color') == color) for k in ('count', 'amount', 'cost')}
