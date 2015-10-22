# Django object is not JSON serializable
categories = ShopCategory.objects.filter(enabled=True, parent=parent_id).values('id', 'title')
json_posts = mark_safe(json.dumps(list(categories), ensure_ascii=False))
