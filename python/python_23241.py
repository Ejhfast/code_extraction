# How to merge multiple returned lists into one
result=[ x for y in (a for a in (funct() for funct in functs) if a) for x in y]
