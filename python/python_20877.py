# django product of annotate
Location.objects.annotate(encounter_count=Count('subject__encounter'))
