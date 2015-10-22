# Python sorting : sub strings
sorted(set(s[a:b] for a in range(n) for b in range(a+1,n+1)),
       key=lambda x:(len(x),x))
