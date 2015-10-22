# Exclude specific email address with regex
results = list_from_your_regex
invalids = ['info', 'server', 'noreply', ...]
valid_emails = [good for good in results if good.split('@')[0] not in invalids]
