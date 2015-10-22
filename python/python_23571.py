# Python eval function with numpy arrays via string input with dictionaries
In [143]: import numexpr as ne
In [146]: ne.evaluate('2*a*(b/c)**2', local_dict=var)
Out[146]: array([ 0.88888889,  0.44444444,  4.        ])
