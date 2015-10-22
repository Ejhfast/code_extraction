# How do I read a text file into a string variable in Python
with open ("data.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')
