# different results for standard deviation using numpy and R
apply(x1, 2, function(x) sd(x) * sqrt((length(x) - 1) / length(x)) )
