# function vs lambda statement
lmb = lambda d: datetime.datetime.strptime(d["Date[G]"]+"-"+d["Time[G]"], "%d-%b-%Y-`%H:%M:%S.%f").strftime("%d-%b-%Y-%H")
