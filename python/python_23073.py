# using regex to replace the value after =
import re
  x="abcdefg=12345"
  print re.sub(r"(.*?)=\d+",r"\1=456789",x)
