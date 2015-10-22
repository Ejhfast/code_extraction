# How do I create loops to substitute for hard-coding window coordinates using Zelle's 'graphics.py' library?
for xCoord in xrange(1, 10):
    for yCoord in xrange(1, 10):
        Text(Point(xCoord , yCoord ), "*").draw(win)
