# Pymongo returning incorrectly when using "$gte" and "$lte"
cursor = db.tweets.find({"tweet.timestamp":{'$gte':startEpoch, '$lte':endEpoch}})
