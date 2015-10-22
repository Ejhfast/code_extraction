# How to use python markdown to process a file that is read in?
f = open('myfile.txt', 'r')
htmlmarkdown=markdown.markdown( f.read() )
