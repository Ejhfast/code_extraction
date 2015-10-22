# Django filter a queryset with field value lookup
&gt;&gt;&gt; from django.db.models import F
&gt;&gt;&gt; Order.objects.filter(received__lt=F('ordered'))
