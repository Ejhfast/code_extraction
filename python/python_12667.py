# Pandas DataFrame: remove unwanted parts from strings in a column
data['result'] = data['result'].map(lambda x: x.lstrip('+-').rstrip('aAbBcC'))
