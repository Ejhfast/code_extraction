# How do you read lines from a .txt file?
with open('numbers.txt') as file:
    lst = [line.strip() for line in file]
