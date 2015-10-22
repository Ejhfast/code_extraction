# Cannot seem to delete an object number
order = models.Order.objects.get(pk=1219)
if request.POST.get('delete'):
    order.delete()
