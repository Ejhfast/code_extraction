# HTTP requests assign multiple values to a key in params
payload = {'topicIds[]': ['128487', '242793']}
r = requests.get(url, params=payload, headers=headers)
