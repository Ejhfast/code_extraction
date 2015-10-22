# Python code can't find cython function eventhough it should not even attempt to find it. Why?
cdef Item item
    for item in self.content:
        result.append(item.export())
