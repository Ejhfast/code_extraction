# Fastest way to scale a list of floats
import numpy
probs = numpy.array([proba[0] for proba in self.classifier.predict_proba(x_test)])
list_values = probs/maximum
