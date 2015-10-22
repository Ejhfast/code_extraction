# Pythonic way to convert a dictionary to a numpy array
import pandas as pd
s = pd.Series({'a':1, 'b':2, 'c':3})
s.values # a numpy array
