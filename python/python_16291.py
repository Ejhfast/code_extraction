# Get list of elements currently in heap using heapq in Python ?
def items(self):
    return list(item for _, _, item in self.heap)
