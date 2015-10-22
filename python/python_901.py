# Generate two lists at once
aprime, bprime = zip(*[(a1,b1) for a1,b1,c1 in zip(a,b,c) if c1==0])
