# Django model inheritance - only want instances of parent class in a query
places = Place.objects.all()
not_restaurants = [p for p in places if not hasattr(p, 'restaurant')]
