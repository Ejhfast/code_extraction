# How to implement callable distance metric in scikit-learn?
cluster = DBSCAN(eps=1.0, min_samples=1,metric=lambda X, Y: distance.normalized_euclidean(X, Y, SD=stdv))
