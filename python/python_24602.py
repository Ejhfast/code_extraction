# how to update data into table in sql database using django
Entry.objects.filter(pub_date__year=2007).update(headline='Everything is the same')
