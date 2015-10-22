# Python script to convert from UTF-8 to ASCII
data="UTF-8 DATA"
udata=data.decode("utf-8")
asciidata=udata.encode("ascii","ignore")
