# Python Pandas Panel counting value occurence
for dataset in P:
        abc = P.loc[dataset,:,'b']
        abc_low = sum(i &lt; 1.0 for i in abc)
