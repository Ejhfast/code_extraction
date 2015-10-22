# python re split string by alpha digit and symbol
&gt;&gt;&gt; s =  'asdf123Acx*23 #'
&gt;&gt;&gt; re.findall(r'[A-Za-z]+|\d+|\W+', s)
['asdf', '123', 'Acx', '*', '23', ' #']
