# Reading CSV data with yearday column into Pandas as datetime
def parse(hr, mn, sec, yearday, yr):
          date_string = ' '.join([yr, yearday, hr, mn, sec])
          return dt.datetime.strptime(date_string, "%Y %j %H %M %S")
