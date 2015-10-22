# Create variable names on demand
rooms = dict(('room_%d' % x, Room(x)) for x in range(1, 6))
