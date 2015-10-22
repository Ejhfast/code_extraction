# How do I calculate the date six months from the current date using the datetime Python module?
import datetime
print (datetime.date.today() + datetime.timedelta(6*365/12)).isoformat()
