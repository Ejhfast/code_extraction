# Transform result session.query to Object
tq = session.query(Tweet).order_by(desc(Tweet.tweet_id_uniq)).first()
