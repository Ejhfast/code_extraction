# Most efficient way to open a file and read the lines?
with open('vlgaChcWaves.txt', 'r+') as vlgaStream:
  for line in vlgaStream:
    dosomethingwith(line)
