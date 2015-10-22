# Python regular expression grabbing a middle number
import re
m = re.search(r"-?\d+\.?\d+\s+(-?\d+\.?\d+)\s+-?\d+\.?\d+", "53.4 -63.2 433.2")
print(re.group(1))
