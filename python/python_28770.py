# How do I get date and time from two columns of a numpy array into a datetime format that can be used by matplotlib?
dtfix=[dt.datetime.strptime(x, "%m/%d/%y %H:%M:%S") for x in dtcode]
