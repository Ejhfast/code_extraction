# A pythonic way to solve the following implementation
Review.objects.values(company, website__website_type).annotate(review_count=Count('id'), average=Avg('rating')).order_by('company')
