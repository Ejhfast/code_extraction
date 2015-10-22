# Django group by to find the count
pages = Page.objects.annotate(num_countries=Count('country'))
pages[0].num_countries  # 3
pages[1].num_countries  # 4
