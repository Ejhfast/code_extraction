# Django split the word and stored in database table
for skill in keyskills.split(','):
  employerkeyskills.objects.create(emp=..., job=..., keyskills=skill)
