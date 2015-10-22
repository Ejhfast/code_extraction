# Django - Following a foreign key relationship (i.e JOIN in SQL)
u = Table1.objects.get(id=1)
print u.id
print u.user.user_name
