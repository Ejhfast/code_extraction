# counting self referencing many to many field
qs = qs.annotate(number_of_supporters=Count('supporters'))
 qs = qs.order_by('-number_of_supporters')
