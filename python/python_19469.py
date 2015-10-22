# Python: index of first non-matching character?
&gt;&gt;&gt; next(i for (i, e) in enumerate("aaaaaxcbaa") if e != "a")
5
