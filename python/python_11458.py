# Display a string of 1's and 0's in binary format Python
data = " ".join(bin(ord(b))[2:].rjust(8, "0") for b in data)
