# How to query mongoDB using Mongoengine with several "WHERE" arguments (what is AND)?
queryResults = Event.objects(title__icontains=q, end__gte=datetime.utcnow())
