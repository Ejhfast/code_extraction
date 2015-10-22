# how to parse the file?
string = open('file_with_string.html', 'r').read()
doc = lxml.html.document_fromstring(string)
