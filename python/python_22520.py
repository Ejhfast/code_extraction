# MultinomialNB in python/pandas returns "objects are not aligned" error when predicting
subcount=count_vectorizer.transform(["this is a test subject"])
classifier.predict(subcount)
