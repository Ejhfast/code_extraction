# Join in Django views
Model2.objects.filter(pk__in=Model1.objcts.values_list('post_id', flat=True)).values('p_slug')
