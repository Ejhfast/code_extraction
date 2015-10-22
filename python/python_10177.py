# dynamically generate css content not taking effect
string = u'#exampleTextInput{ background-color:#ff0000;}\n'
return HttpResponse(string, content_type='text/css')
