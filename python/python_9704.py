# numpy equivalent of MATLAB spones
x = ... some sparse matrix ...
y = x.copy().tocsr()
y.data.fill(1)
