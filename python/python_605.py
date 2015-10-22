# Getting all items less than a month old
from datetime import datetime, timedelta
last_month = datetime.today() - timedelta(days=30)
items = Item.objects.filter(my_date__gte=last_month).order_by(...)
