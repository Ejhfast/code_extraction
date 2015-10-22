# list comprehension of a nested for loop
with open('tabdelim.txt') as rows:
    lstcmp = [item for row in rows for item in row.strip().split('\t')]
    print('\n'.join(lstcmp))
