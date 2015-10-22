# Multiple Element Indexing in multi-dimensional array
&gt;&gt;&gt; np.mean(myarray[np.arange(5)[:, None, None], np.array(yy)[:, None], xx],
            axis=(-1, -2))
array([ 0.49482768,  0.53013301,  0.4485054 ,  0.49516017,  0.47034123])
