# How to nullify a django datetime field that has an existing value?
order = Order.objects.get(pk=99)
order.fulfilled = None
order.save()
