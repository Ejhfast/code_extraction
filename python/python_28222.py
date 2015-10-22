# easy method for spliting substrings of a given length from a string
&gt;&gt;&gt; s = 'AGTAATGGCGATTGAGGGTCCACTGTCCTGGTAC'
&gt;&gt;&gt; [s[i:i+6] for i in range(len(s)-5)]
['AGTAAT', 'GTAATG', 'TAATGG', 'AATGGC', 'ATGGCG', 'TGGCGA', 'GGCGAT', 'GCGATT', 'CGATTG', 'GATTGA', 'ATTGAG', 'TTGAGG', 'TGAGGG', 'GAGGGT', 'AGGGTC', 'GGGTCC', 'GGTCCA', 'GTCCAC', 'TCCACT', 'CCACTG', 'CACTGT', 'ACTGTC', 'CTGTCC', 'TGTCCT', 'GTCCTG', 'TCCTGG', 'CCTGGT', 'CTGGTA', 'TGGTAC']
