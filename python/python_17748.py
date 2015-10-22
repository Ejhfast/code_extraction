# How to move an item in a list two units down
def move (l, from_, to = 2):
    return l.insert (to, l.pop (from_) )
