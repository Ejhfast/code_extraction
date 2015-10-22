# How do I load an index (Dow, Nasdaq) with Zipline?
data = load_from_yahoo(stocks=['AAPL', '^gspc', '^ixic'], indexes={}, start=datetime(2014, 1, 1), end=datetime(2015,4,2))
