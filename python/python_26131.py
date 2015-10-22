# Loops for sequence output - python
width = 6
for i in range(len(sequence) - width):
    print " " * i + sequence[i:i+width]
