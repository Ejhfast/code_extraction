# Django: Necessary html-page in views
return render(request, 'blog/articles/{}.html'.format(pk), {'article': article})
