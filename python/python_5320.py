# serialize datetime to json in Django
from django.core.serializers.json import DjangoJSONEncoder
 data =  json.dumps(data, cls=DjangoJSONEncoder)
