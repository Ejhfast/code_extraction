# data = My_Model.objects.extra(select=select_data).values('d').annotate(Sum("numbers_data")).order_by()
