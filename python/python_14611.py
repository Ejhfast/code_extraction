# Django model - Updating a attribute without touching lastmodified_at
class ArticleViewCount(model):
    counter = models.PositiveIntegerField()
    article = models.OneToOneField(Article)
