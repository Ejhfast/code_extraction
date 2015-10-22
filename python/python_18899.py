# Showing a empty GET form without raising any error on Django
if request.GET:
    form = SearchForm(request.GET)
