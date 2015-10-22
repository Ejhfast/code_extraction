# unsupported operand type(s) for +: 'numpy.ndarray' and 'str'
&gt;&gt;&gt; np.core.defchararray.add(np.arange(5).astype(str), 'th')
array(['0th', '1th', '2th', '3th', '4th'],
      dtype='|S26')
