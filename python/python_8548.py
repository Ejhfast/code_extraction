# Remapping an array of integers
RANGE_SIZE = 255-100
for index in range(256):
     array[index] = 100 + int( RANGE_SIZE * float(index) / 255.0 )
