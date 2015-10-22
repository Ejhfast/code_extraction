# Django unique_together but only for filtering
Sequence.objects.order_by('taxonomy', 'sequence').distinct('taxonomy', 'sequence')
