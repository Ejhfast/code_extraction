# How to loop over a circular list, while peeking ahead and behind current element?
for i, e in enumerate(L):
    print(e, L[i-1], L[(i+1) % len(L)])
