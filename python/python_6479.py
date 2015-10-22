# Creating Multable pyGTK objects based on a list
self.entries = [gtk.Entry(max=0) for objects in object_list]
for entry in self.entries:
  self.vbox_entry.add(entry)
