# How to calculate minimun value in all variables? Python
&gt;&gt;&gt; scores = [Myscore1, Myscore2, Myscore3]
&gt;&gt;&gt; [(x, (x == min(scores))) for x in scores]
[(6, False), (-3, True), (10, False)]
