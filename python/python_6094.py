# looping through list of lists
out = [[coord + float(y) - float(x) for v in V] for x,y in zip(x_coord, y_coord)]
