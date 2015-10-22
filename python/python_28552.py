# how to urlencode a value that is a python dictionary with encoded unicode characters
&gt;&gt;&gt;urllib.urlencode({"param":"val", "items":[json.dumps(item) for item in items] }, True)
