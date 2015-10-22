# Python - Parsing multipart/form-data request on server side
pdict = {'boundary':'*****'}
cgi.parse_multipart(self.request.body_file, pdict)
