# Remove rows with same ID from two lists in Django
checkins.objects.filter( location_id__in = list(flagged_checkins.objects.values_list('location_id', flat=True)) ).delete()
