# Content of text file as a input to python script
with open ("data.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')
