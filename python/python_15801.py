# Get the error code from tweepy exception instance
except tweepy.TweepError as e:
    print e.message[0]['code']  # prints 34
    print e.args[0][0]['code']  # prints 34
