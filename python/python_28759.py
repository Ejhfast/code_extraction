# How to get text between 2 lines with PYthon
data = {i.split()[0]: i.split()[1:] for i in open('PID.txt').read().split('\n\n')}
