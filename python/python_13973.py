# django model inheritance and admin application
class History(Article, IHasAttachments):
    date = DateField(default=datetime.date.today)
