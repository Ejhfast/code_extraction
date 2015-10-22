# How to request all the information from the HTML form in Google App Engine?
# An iterable with alll items in the MultiDict:
# [('check', 'a'), ('check', 'b'), ('name', 'Bob')]
self.request.POST.items()
