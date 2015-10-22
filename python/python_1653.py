# Regex to separate Numeric from Alpha
&gt;&gt;&gt; re.findall('(\d+|[a-zA-Z]+)', '12fgsdfg234jhfq35rjg')
['12', 'fgsdfg', '234', 'jhfq', '35', 'rjg']
