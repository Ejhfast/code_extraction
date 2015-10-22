# Pythonic mapping of an array (Beginner)
for char in sys.argv[1].lower():
  print nato.get(char, char) # try to get nato[char] otherwise return char
