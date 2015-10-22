# Django: using the URL request as the name of a model's field
word = Word.objects.get(...)
setattr(word, fieldName, True)
