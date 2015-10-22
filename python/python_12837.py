# Python: Dumping Database Data with Peewee
for field in User._meta.get_sorted_fields():
    print field.name
