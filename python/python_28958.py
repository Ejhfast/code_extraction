# Removing strings from a list that contain dates, without effecting stand alone dates in the list
tempDates = ['Date', 'Visitor', 'Home', 'Notes', '2013-10-01', 'Washington Capitals', 'Chicago Blackhawks', None, '2013-10-01', 'Winnipeg Jets','...', 'St. Louis Blues','...', 'Postponed due to blizzard until 2014-02-25', 'etc']
print [i for i in tempDates if re.match(r"\d{4}-\d{2}-\d{2}",str(i))]
