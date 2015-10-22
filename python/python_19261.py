# How do I count only weekdays from timedelta in python
from dateutil.rrule import *
    number_weekdays = rrule(WEEKLY, byweekday=(MO,TU,WE,TH,FR), dtstart=datetime.utcnow(),until=dt).count()
