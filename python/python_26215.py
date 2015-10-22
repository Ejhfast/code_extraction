# Python -- making a dict out of a string
s = 'home_id: [redacted] id: [7] name: [] model: []'
d = dict([pair.strip().split(': [') for pair in s.split(']') if pair])
