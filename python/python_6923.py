# Sorting a python dictionary by name?
location_map_india = sorted(location_map_india.iteritems(), key=lambda x: x[1]["name"])
