# Faster float to int conversion in Python
def floatToInt(x):
    return int((x+1.0) * (2**31))
