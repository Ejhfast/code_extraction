# Python: 'Unmask' a long XOR'd string of data
frame = bytearray(frame)
for i in range(len(mask)):
    frame[i] ^= mask[i]
