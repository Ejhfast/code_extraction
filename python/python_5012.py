# How to write unicode strings into a file?
s = u'\u5E73\u621015'
with open("yop", "wb") as f:
   f.write(s.encode("UTF-8"))
