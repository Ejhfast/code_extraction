# How do I find out the size of a canvas item in Python/Tkinter?
bounds = self.canvas.bbox(myText)  # returns a tuple like (x1, y1, x2, y2)
width = bounds[2] - bounds[0]
height = bounds[3] - bounds[1]
