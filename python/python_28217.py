# Filtering Tweets By Location
if len( jd['coordinates'] ) &gt; 1:
    self.db.tweets.insert( { 'text' : jd['text'], 'coordinates' : jd['coordinates'], 'lang' : jd['lang'] } )
