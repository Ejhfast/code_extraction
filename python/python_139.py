# Django equivalent for count and group by
query_set = Item.objects.extra(select={'count': 'count(1)'},
                               order_by=['-count']).values('count', 'category')
query_set.query.group_by = ['category_id']
