# Python Regex split text file into sentences and append to a list
text_file= open(filename,'r')
data=text_file.read()
listOfSentences = data.split(".")
