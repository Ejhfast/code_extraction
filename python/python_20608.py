# converting from numpy array of one type to another by re-interpreting raw bytes
In [85]: x.view('&lt;i2')
Out[85]: array([ 20329,  13764, -20329, -13765,    249,   1743], dtype=int16)
