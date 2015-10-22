# Annotation not displaying/working properly
most_injured = Player.objects.annotate(injury_count=Count('playerinjury')).order_by('-injury_count')[:5]
