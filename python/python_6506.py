# Simple idiom to break an n-long list into k-long chunks, when n % k > 0?
[x[i:i+k] for i in range(0,n,k)]
