# Django GROUP_BY through .annotate()
Customer.objects.annotate(buy_count=Count('invoice')).all()
