# Django Queryset for date
from datetime import datetime, timedelta
Example.objects.filter(date_created__lte=datetime.utcnow() -
                          timedelta(days=6*30)).delete()
