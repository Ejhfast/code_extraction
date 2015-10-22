# How to get the values in split python?
&gt;&gt;&gt; l = ['column1:abc,def', 'column2:hij,klm', 'column3:xyz,pqr']
&gt;&gt;&gt; [item.split(":")[1].split(',') for item in l]
[['abc', 'def'], ['hij', 'klm'], ['xyz', 'pqr']]
