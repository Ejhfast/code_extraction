# Python 2.7.2 Ubuntu + Django 1.4; deepcopy recursion error when ".objects.get(foo=unicodestr)"
try:
    Uebersetzung.objects.get(artikel=unicode(each[0]),deutsch=unicode(each[1]),turk=unicode(each[2]))
