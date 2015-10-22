# Integrity Error in Django 1.7
obj, created = Person.objects.update_or_create(
    first_name='John', last_name='Lennon', defaults=updated_values)
