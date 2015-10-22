# Add column to DataFrame in rpy2
d = ro.r.cbind(d, cum_misses=ro.r.cumsum(d.rx2('misses')))
