# Inserting tweets into MySQL DB using Tweepy
c.execute("INSERT INTO tweets (tweet_time,     username, tweet) VALUES (%s,%s,%s)" ,
              (time.time(), username, tweet))
