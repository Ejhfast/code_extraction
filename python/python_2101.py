# How do I sort this list in Python, if my date is in a String?
.sort(key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d'))
