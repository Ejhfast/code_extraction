# Django. Order by filtered backward related field
Parent.objects.filter(child__name='defined name').order_by('child__value')
