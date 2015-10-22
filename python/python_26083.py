# Extract single True/False value from JSON Twitter response ( Tweepy and Python )
print json.loads(api.show_friendship(target_id=user_id))["relationship"]["target"]["followed_by"]
