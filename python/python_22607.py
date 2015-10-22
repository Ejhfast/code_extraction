# unpack multiple lists when calling a function
&gt;&gt;&gt; from itertools import chain
&gt;&gt;&gt; pack(5, 6, *chain(L1, L2))
