# Replace everything but digits
&gt;&gt;&gt; s = 'Promo 77'
&gt;&gt;&gt; "".join(i for i in s if i.isdigit())
'77'
