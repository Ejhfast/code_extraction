# Class assigning index to object using static class variable
def get_index(self):
     SetObject.object_counter += 1
     return SetObject.object_counter-1
