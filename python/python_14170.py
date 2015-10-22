# How would I search for values in a dictionary?
if 'error' in self.dict1:
    raise ValueError("%s: %s" % (self.dict1["error"], self.dict1["message"]))
