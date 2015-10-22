# Group by, distinct, count in django
from django.db.models import Count
Usage.objects.filter(no_of_people_house='4', city='HYDERABAD', nursing_cnt='2ND TIME MOTHER', bucket='BRAND PENETRATION').values('final_category').annotate(responders=Count('responders'))
