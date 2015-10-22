# Grouping by a ForeignKey, and ForeignKeys that are another 'step' away
Artist.objects.annotate(played=Count('song__songplay')).order_by('-played')[:10]
Song.objects.annotate(played=Count('songplay')).order_by('-played')[:10]
