# Rejecting zero values when creating a list of minimum values. (Python Field Calc)
def my_min(d1,d2,d3,d4):
    lst = [d1,d2,d3,d4]
    return min([x for x in lst if x !=0])
