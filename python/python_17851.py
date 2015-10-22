# Encode rows of boolean numpy array to bytes
&gt;&gt;&gt; np.packbits(np.uint8(x))
array([204,  12, 128], dtype=uint8)
