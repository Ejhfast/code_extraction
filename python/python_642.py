# Django model query with custom select fields
.extra(select={'is_staff': "%s.name='staff'" % Permission._meta.db_table, 'is_student': "%s.name='student'" % Permission._meta.db_table, })
