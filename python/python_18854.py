# Can sed write few outputs for the same input?
&gt;&gt;&gt; " ".join("ab" + "d"*i + "c" for i in range(1, 5))
'abdc abddc abdddc abddddc'
