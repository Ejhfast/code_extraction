# MongoDB using an OR clause in mongoengine
query = ContentItem.objects.filter( (Q(account=account) and Q(public=True)) or  (Q(account=account) and Q(creator=logged_in_user)) ).order_by('-last_used')
