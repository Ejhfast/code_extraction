# How to Handle JSON with escaped Unicode characters using python json module?
data = jsDat.get('data')
data = data.encode('ascii', 'ignore')
