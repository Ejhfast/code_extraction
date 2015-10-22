# how to Skip None holding tuple in list?
&gt;&gt;&gt; [x for x in listobj if any(y is not None for y in x)]
[(None, None, '01/02/2015', '25'), (None, None, '01/02/2015', None), (0, None, None, None)]
