# How to move each figure toward the goal between the poin that I click on graphics and the center of my object in Python
def move(obj, goal):
    obj.x = ((obj.x - goal.x) * 15.0 / 16) + goal.x
    obj.y = ((obj.y - goal.y) * 15.0 / 16) + goal.y
