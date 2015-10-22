# Django query a model since its creation to an X time
import datetime
HelpRequest.objects.filter(creation_time__gte=(datetime.datetime.now() - datetime.timedelta(minutes=5)))
