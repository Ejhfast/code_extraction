# Efficient way to loop through numpy array
whr = numpy.where( (col &lt; ...) &amp; (col &gt; ...) &amp; (row &lt; ...) &amp; (row &gt; ...))
for rr,cc in zip(row[whr],col[whr]):
