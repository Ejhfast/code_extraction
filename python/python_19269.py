# Recording and writing voice data as String in a file for Encryption
with open("filename", 'w') as outFile:
  for frame in frames:
    outFile.write(frame)
