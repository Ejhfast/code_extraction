# Using python to write hex to file
for i in range(2**8):
    with open("test" + str(i) + ".bin", "wb") as f:
        f.write(chr(i))
