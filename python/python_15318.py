# grid search cross-validation on SVC probability output in sci-kit learn
class ProbSVC(SVC):
    def predict(self, X):
        return super(ProbSVC, self).predict_proba(X)
