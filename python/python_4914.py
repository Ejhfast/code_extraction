# Updating a python Tkinter frame
self.countStr = StringVar()
self.countStr.set(str(self.count))
Label(self.countFrame, textvariable=self.countStr).pack(side=RIGHT, padx=5)
