# Python open() raises an error if I try to create a file
f=open("nonexistent.txt","w")
f.write('Test')
f.close()
