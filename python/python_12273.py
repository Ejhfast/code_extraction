# Python function to build list from a text file
def eventfreq(year, month):
    dates = [dt for x, dt, y in fieldict('DOT1000.txt') if dt.year==year and dt.month==month]
    return [(dt, dates.count(dt)) for dt in set(dates)
