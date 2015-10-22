# 2 digit years using strptime() is not able to parse birthdays very well
if d &gt; datetime.now():
    d = datetime(d.year - 100, d.month, d.day)
