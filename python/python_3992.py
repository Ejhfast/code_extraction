# python unicode: How can I judge if a string needs to be decoded into utf-8?
if not isinstance(data, unicode):
    # It's not Unicode!
    data = data.decode('UTF8')
