# How to retrieve a distribution of values for a models field using Django?
from django.db.models import Count
Answer.objects.all().values('question', 'points_achieved').annotate(total=Count('points_achieved')).order_by('total')
