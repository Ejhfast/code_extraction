# Python - how can I address an array along a given axis?
idx = [slice(None)] * array.ndim
idx[axis] = slice(start, end)
myslice = array[tuple(idx)]
