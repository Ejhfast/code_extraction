# sorting strings based on your own values in python
suits = {'queen': 2, 'jack': 1, 'king': 2}
l = ['queen','jack','king']
print sorted(l, key=suits.get)
