# python: send value of a variable instead of its name to function
rank=Rank()
for att in attributes:
     setattr(rank, att, somevalue)
