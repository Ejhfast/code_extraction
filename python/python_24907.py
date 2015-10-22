# .arff files with scikit-learn?
import arff, numpy as np
dataset = arff.load(open('mydataset.arff', 'rb'))
data = np.array(dataset['data'])
