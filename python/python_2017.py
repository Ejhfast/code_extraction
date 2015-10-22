# Python - Nested List to Tab Delimited File?
with open('fname', 'w') as file:
    file.writelines('\t'.join(i) + '\n' for i in nested_list)
