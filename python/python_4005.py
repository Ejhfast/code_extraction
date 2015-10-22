# Trying to use MEGAM as an NLTK ClassifierBasedPOSTagger?
maxent_tagger = ClassifierBasedPosTagger(train=train_sents, classifier_builder=lambda train_feats: MaxentClassifier.train(train_feats, algorithm='megam', max_iter=10, min_lldelta=0.1))
