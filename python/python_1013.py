# Percentage with variable precision
import math
def format_percentage(x, precision=3):
    return ("%%.%df%%%%" % (precision - min(0,math.log10(100-x)))) % x
