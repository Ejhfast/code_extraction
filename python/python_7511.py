# filtering input from serial port data
def purifystring(string_to_analyze):    # string is a really bad variable name as it is a python module's name
   return "".join(digit for digit in string_to_analyze if digit.isdigit())
