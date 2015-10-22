# django, group model by days
query = Game.objects.all().query
query.group_by = ['date']
results = QuerySet(query=query, model=Game)
