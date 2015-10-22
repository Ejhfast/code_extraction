# Django/Python: how can i filter with Model's custom method?? Is this possible?
import datetime
queryset = MyModel.objects.filter(\
     time_created__lt=(datetime.now()-datetime.timedelta(minutes=3)))
