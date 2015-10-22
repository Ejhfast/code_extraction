# concatenate numpy arrays that are class instance attributes in python
def concatenate_attributes(self):
    self.a = np.hstack([o.a for o in self.my_class_inst])
    self.arr = np.hstack([o.arr for o in self.my_class_inst])
