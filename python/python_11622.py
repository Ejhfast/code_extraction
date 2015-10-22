# Django ORM & hstore : counting unique values of a key
Item.objects.extra(
    select=dict(key = "content_item.data -&gt; 'key'")
).values('key').order_by('key').annotate(total=Count('key'))
