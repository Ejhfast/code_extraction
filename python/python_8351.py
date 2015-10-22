# Creating a room for a dungeon gives wrong dimensions/no walls
def makeFloor(Xmax, Ymax):
    return [[Cell(solid,None) for i in range(Xmax)]
            for j in range(Ymax)]
