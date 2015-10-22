# turn a list of strings into a list of xyz cooridnates python
points= [list(map(int,v.split())) if v.strip().lower() != "j" else "JUMP" for v in vlist]
