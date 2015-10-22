# What's the best django way to do a query that spans several tables?
Recommendation.objects.filter(user__publication_set__subscriber=request.user).select_related()
