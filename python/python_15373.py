# Changing Canvas Fill inside Application
self.id = self.canvas1.create_oval(..., fill="green")
...
self.canvas1.itemconfigure(self.id, fill="black")
