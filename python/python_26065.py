# python 2.7 - CountVectorizer error :AttributeError: 'file' object has no attribute 'lower'
count_vect = CountVectorizer(input="file")
X_train_counts = count_vect.fit_transform(list1)
