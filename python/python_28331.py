# python splitting string twice
&gt;&gt;&gt; a = '{1;5}{2;7}{3;9}{4;8}'
&gt;&gt;&gt; [item.split(';') for item in a[1:-1].split('}{')]
[['1', '5'], ['2', '7'], ['3', '9'], ['4', '8']]
