# one-many relationship-google datastore-python
key = db.Key.from_path('food', 'apple')
reviews = FoodReview.all().filter("reviews =", key)
