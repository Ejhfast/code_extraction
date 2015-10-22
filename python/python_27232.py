# How can you tell if numbers in a list are bigger than 126? If it is bigger the program needs to add 94 to it
for i, element in enumerate(addOffset):
    if element &gt; 126:
        addOffset[i] = element + 94
