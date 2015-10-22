# Convert C++ '? :'conditional operators into python
def easeInExpo( t, b, c, d ):
    return b if t == 0 else c * pow( 2, 10 * (t/d - 1) ) + b
