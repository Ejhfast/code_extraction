# Creating links to django views using HTMLCalendar
def formatmonth(self, year, month):
    self.year, self.month = year, month
    return super(EventsCalendar, self).formatmonth(year, month)
