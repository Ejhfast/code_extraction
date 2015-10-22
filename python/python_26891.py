# Python - extract lines between multiple instances of the same delimiter
with open('input.txt') as input_file:
    result = input_file.read().split('===\n')
print result
