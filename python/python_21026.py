# Why change buffersize of open function to 0 to prevent the loss of data while writing to file in python?
with open('filename', 'w') as fr:
     for x in lines:
         fr.write(str(x) + ' ')
