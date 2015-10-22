# Error in sympy.solve on Freudenstein equation
&gt;&gt;&gt; eq=3.2*cos(x+.2)+1.7
&gt;&gt;&gt; [w.n(3,chop=True) for w in solve(expand(eq.rewrite(exp)))]
[-2.33, 1.93]
