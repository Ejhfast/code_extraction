# How to make a Group by and order by max(...) in django
cat_pub = Publicacion.objects.all().values('id_categoria').annotate(max_update_time=Max('update_time')).order_by('-max_update_time')
