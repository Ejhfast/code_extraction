# Django retrieving a tables data based on another table
Note.objects.all().order_by('note_data__created')
