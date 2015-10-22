# how to get the second word of an element in a list
def lookup_bus_stop_by_road_name(bus_stops, name):
    return [bus_stop for bus_stop in bus_stops if name.lower() in bus_stop[1].lower()]
