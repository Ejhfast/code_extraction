# Use wxPython.FileDialog to save file
with open(self.save_path, "wb") as file:
    writer = csv.writer(file, delimiter = ',')
