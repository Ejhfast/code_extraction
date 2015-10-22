# Finding valid neighbor indices in 2d array
valid={(x,y) for x in range(3) for y in range (3)}
dirs=[(dx,dy) for dx in (-1,0,1) for dy in (-1,0,1) if (dx,dy)!=(0,0)]
def voisins(x,y): return [(x+dx,y+dy) for (dx,dy) in dirs  if (x+dx,y+dy) in valid]
