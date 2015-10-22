# django many to many field annotate and count
from django.db.models import Count
un_list = Question.objects.annotate(a_count=Count("answer")).filter(a_count=0)
