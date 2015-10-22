# Build a dictionary from successful regex matches in python
file_data = open('x:\\path\\to\\file','r').read()
my_list = re.findall(pattern, file_data, re.MULTILINE)
my_dict = {c:b for a,b,c in my_list}
