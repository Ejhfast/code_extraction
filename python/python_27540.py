# Recover named features from L1 regularized logistic regression
features = pipeline.named_steps['tfidf'].get_feature_names()
print(features[pipeline.named_steps['l1'].coef_ != 0])
