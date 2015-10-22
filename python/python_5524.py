# Python - convert comma separated string into reducing string list
location_in  = 'London, Greater London, England, United Kingdom'
locations    = location_in.split(', ')
location_out = [', '.join(locations[n:]) for n in range(len(locations))]
