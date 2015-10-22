# Django: ordering by specific backwared related property
Video.objects.filter(translations__language='en').order_by('translations__name')
