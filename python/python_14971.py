# How to represent class labels in Python for training a multi-label classifier with non-binary feature values in NLTK?
[(list(movie_reviews.words(fileid)), category)
...              for category in movie_reviews.categories()
...              for fileid in movie_reviews.fileids(category)]
