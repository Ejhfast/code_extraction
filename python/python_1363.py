# Add tuple to list of tuples in Python
result = [(x+dx, y+dy) for x,y in points for dx,dy in offsets]
