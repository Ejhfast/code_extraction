# Finding MIN & MAX values across 3 different dictionaries
minstat = {}
for month in stat2011:
    minstat[month] = min(stat2011[month], stat2012[month], stat2013[month])
