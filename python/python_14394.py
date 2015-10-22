# DISTINCT ON in django
OrderNotes.objects.filter(item=item).values_list('shared_note', flat=True).distinct()
