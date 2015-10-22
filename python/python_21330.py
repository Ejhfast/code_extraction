# setting justOne limiter for pymongo remove throws TypeError
ufo.users.remove({'emails.address': 'foo@bar.com'}, safe=True)
