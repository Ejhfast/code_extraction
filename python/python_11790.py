# Select within select using Django ORM
SomeModel2.objects.annotate(new_field=Count('SomeField2',
    distinct=True)).filter(condition=condition,
    another_condition=condition2).values('new_field', 'Somefield1')
