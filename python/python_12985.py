# ValueError: time data '22.12.2012 17:00' does not match format '%d.%m.%Y %I:%M', am/pm
import datetime
datetime.datetime.strptime("22.12.2012 17:00", '%d.%m.%Y %H:%M')
