# eliminating redundant tuples
set([(a,b,c) if a&lt;b else (b,a,c) for a,b,c in tups])
