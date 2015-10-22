# How can I more easily save value in txt file to variable? python line.split
with open('somefile') as fin:
    points = [line.split()[1] for line in fin if line.startswith('something')]
