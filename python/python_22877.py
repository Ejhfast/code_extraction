# Django JOIN eliminates desired columns
questions = Question.objects.select_related().filter(vote__creator=3).values()
