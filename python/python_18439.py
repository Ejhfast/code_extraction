# Python: How to only loop over first 'x' items of a very long list; Writing a Twitter bot with tweepy
# Only iterate through the first 200 followers
for follower in Cursor(api.followers).limit(200):
     follower_ids.append(follower.id)
