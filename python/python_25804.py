# What is the equivalent python script of Linux command "strings"?
print re.findall("[a-zA-Z0-9]+",open("some_file.data","rb").read())
