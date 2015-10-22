# how to append the content of one file at the of the content of another file in python
with open("test1.txt","a") as file1, open("test2.txt","r") as file2:
    for line in file2:
        file1.write('\n' + line)
