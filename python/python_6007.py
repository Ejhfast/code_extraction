# Django Python noob - how do I get the NUMBER out of a Aggregate sum?
tot=PurchaseOrderLine.objects.aggregate(total=Sum('price'))['total']
return HttpResponse(tot)
