# Django ORM, group by day
Product.objects.extra(select={'day': 'date( date_created )'}).values('day') \
               .annotate(available=Count('date_created'))
