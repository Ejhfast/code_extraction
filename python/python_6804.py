# Filtering on Foreign Keys in Django
blog_list = Blog.objects.filter( town__country__country_name = 'Canada' ).order_by( '-id' )
