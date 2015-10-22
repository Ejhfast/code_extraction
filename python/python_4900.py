# How to save a ForeignKey without retrieving the foreign object instance?
UserLocale.objects.create(user=user_instance, locale_id=locale)
