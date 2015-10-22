# How to remove thousands separator dot from the formatted numbers
&gt;&gt;&gt; a=["10.000","20.000","25.000"]
&gt;&gt;&gt; [ i.replace(".","") for i in a ]
['10000', '20000', '25000']
