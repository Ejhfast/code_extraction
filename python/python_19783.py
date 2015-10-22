# Django 1.4 - django.db.models.FileField.save(filename, file, save=True) produces error with non-ascii filename
file.save(filename.encode('utf-8', 'ignore'), file, save=True)
