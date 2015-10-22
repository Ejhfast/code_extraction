# Check in Python if URL exists
print requests.get(url, headers=headers).status_code
