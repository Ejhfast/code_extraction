# How to convert SQL Query result to PANDAS Data Structure?
from pandas import DataFrame
df = DataFrame(resoverall.fetchall())
df.columns = resoverall.keys()
