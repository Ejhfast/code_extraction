# heapq.nlargest index of returned result in original sequence
&gt;&gt;&gt; seq = [100, 2, 400, 500, 400]
&gt;&gt;&gt; heapq.nlargest(2, enumerate(seq), key=lambda x: x[1])
[(3, 500), (2, 400)]
