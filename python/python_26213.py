# CountVectorizer in sklearn with only words above some minimum number of occurrences
vect= CountVectorizer(ngram_range=(1,2), binary =True, min_df = 500)
