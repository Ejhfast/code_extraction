# django model filter field of a field
PopularArticle.objects.filter(article__public=True, article__draft=False)
