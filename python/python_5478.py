# Django Models Group By
XML_table.objects.filter(suid='2').values('pid').annotate(docs=Count('pid')).order_by()
