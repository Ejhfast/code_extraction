# Python - iterate through list in threaded script
for ticker in tickers:
   t = Thread(target = quotes, args = (ticker,) )
