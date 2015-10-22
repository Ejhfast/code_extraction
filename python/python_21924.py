# How to return from function nicely when multiple return values expected
result = myFunct(5)
var_1, var_2 = (None, None) if result is None else result
