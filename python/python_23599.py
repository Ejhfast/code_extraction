# Closest equivalent to SUM in Django
from django.db.models import Manager
result = Manager.raw(u"""select SUM(royalty_price*conversion_to_usd)from sales_raw where date='2012-06-01'""")
