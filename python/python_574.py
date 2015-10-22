# Python IRC bot and encoding issue
data = irc.recv ( 4096 )
try: data = str(data,"UTF-8")
except UnicodeDecodeError: data = str(data,"CP1252")
