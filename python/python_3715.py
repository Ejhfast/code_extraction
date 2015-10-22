# Python list sort in descending order
timestamp.sort(key=lambda x: time.strptime(x, '%Y-%m-%d %H:%M:%S')[0:6],
    reverse=True)
