# Django: How to limit number of objects returned from a model
news = News.objects.order_by("-date")[:10]
