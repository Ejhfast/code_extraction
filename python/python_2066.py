# figuring out objects created 30 min ago in django
import datetime
created_time = datetime.datetime.now() - datetime.timedelta(minutes=30)
old_objects = MyModel.objects.filter(created__lte=created_time)
