# Memory error while slicing an array
&gt;&gt;&gt; data = d[:, :, 0].astype(np.short)
&gt;&gt;&gt; data[data==-32768] = data[data&gt;0].min()
&gt;&gt;&gt; data = data.astype(np.float32)
