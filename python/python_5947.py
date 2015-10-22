# How do I use the pearsonr function in scipy to find the correlation and P-Value of dictionary values?
a = [float(x) for x in histodict[str(start)].itervalues()]
b = [float(x) for x in histodict[str(end)].itervalues()]
print pearsonr(a,b)
