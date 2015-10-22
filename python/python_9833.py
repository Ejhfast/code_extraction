# Django: filtering order_by a generic relation
Category.objects.filter(translations__language='en').order_by("translations__text")
