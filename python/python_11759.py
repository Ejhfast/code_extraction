# How to get time 17:00:00 today or yesterday?
test = datetime.datetime.now().replace(hour=17,minute=0,second=0,microsecond=0)
if datetime.datetime.now() &lt; test:
    test = test - datetime.timedelta(days=1)
