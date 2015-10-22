# Django: get related set from a related set of a model
Page.objects.filter(chapter__book=my_book)
