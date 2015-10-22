# Remove dot at the end of number
with open('filename') as f:
    file_data = [[int(float(i)) for i in line.split(',')] for line in f]
