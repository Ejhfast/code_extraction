# memory management: open vs string-building
with open(dest, "a") as file:
    for tweet in iterator_that_returns_tweets:
        file.write(json.dumps(tweet) + "\n")
