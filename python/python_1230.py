# How to loop until EOF in Python?
for block in iter(lambda: file_obj.read(4), ""):
  use(block)
