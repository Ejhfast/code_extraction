# How to create a very large file cheaply using Python in Windows 7?
with open("file.to.create", "w") as file:
    file.truncate(10 ** 10)
