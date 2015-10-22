# Django/Python update field values (during model save)
for field in ['first_name', 'last_name']:
    value = getattr(self, field)
    setattr(self, field, value.title())
