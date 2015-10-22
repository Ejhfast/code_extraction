# Procedure for explicit type conversion in python from a float to int
import math
int(math.round((((year2 - year1) * 12) + (month2 - month1)) * 30.4375 + (day2 - day1)))
