# Python Hashing with lists
def insert(self, key):
    self.slots[self.hash_function(key)].append(key)
