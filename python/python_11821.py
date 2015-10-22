# Find the number of follower using tweepy
loc = [tweepy.api.get_user(friend).followers_count for friend in lof]
