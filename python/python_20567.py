# Scikit-learn Ridge classifier: extracting class probabilities
d = clf.decision_function(x)[0]
probs = np.exp(d) / np.sum(np.exp(d))
