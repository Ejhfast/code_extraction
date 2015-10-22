# How to make calendar date book python
for month, days in zip(monthNames, daysInMonth):
    for day in range(1, days + 1):
        print "%3s %8d" % (month, day)
