# Appending associative arrays in Python
if user not in data:
    data[user] = []
data[user].append({'item': row[0], 'time': row[1]})
