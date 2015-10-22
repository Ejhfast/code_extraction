# Very basic formatting Issue
&gt;&gt;&gt; x = [(10, 20), (50, 60), (100, 110)]
&gt;&gt;&gt; ','.join('-'.join(map(str, t)) for t in x)
'10-20,50-60,100-110'
