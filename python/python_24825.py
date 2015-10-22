# Add "0" to number in strings if they have two digits only
&gt;&gt;&gt; ["data_s{:0&gt;3}".format(x[6:]) for x in s]
['data_s001', 'data_s099', 'data_s133']
