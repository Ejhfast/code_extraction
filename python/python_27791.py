# How to load a image into a label without saving to hard drive python Tkinter
for item in self.images:
    item.seek(0) # set file position back to the start
    img = ImageTk.PhotoImage(Image.open(item))
