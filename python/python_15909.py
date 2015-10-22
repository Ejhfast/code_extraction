# Python - What is the best way to round a float up in magnitude to an integer
def my_rounding(x):
    return math.ceil(x) if x &gt; 0. else math.floor(x)
