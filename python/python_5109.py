# How would I perform this query in Django?
ExternalUser.objects.filter(external_account_id__in=[friend.id for friend in all_friends])
