# Many-to-Many Relationships: Querying for Objects with a Single Value
Album.objects.annotate(n_artists=Count("artists')).filter(n_artists=1).filter(artist=some_awesome_artist)
