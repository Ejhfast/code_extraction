# Sorting strings in python doesnt work
sorted(['a','2%20q'], key=lambda x: 0 if x == '2%20q' else 1)
