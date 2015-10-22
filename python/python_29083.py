# How to read some csv files in a folder in python
import pandas as pd
df = pd.concat([pd.read_csv('file%d.csv' % x) for x in range(1,41)])
df.to_csv('output.csv')
