# Complex django db ordering based on FK properties
from django.db.models import Max
OrderItems.annotate(newest_note_time=Max('ordernotes__timestamp'))
    .order_by('-ordernotes__is_active', '-newest_note_time')
