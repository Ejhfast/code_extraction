# eliminate space between comma and thousands digits in python regex
&gt;&gt;&gt; re.sub(r', (\d{3})', r'\1',original.strip())
'1000000 cases were produced of this, however, that is not important.'
