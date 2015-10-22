# Figure out one Django query
Book.objects.filter(bookquestions__bookanswered__user=request.user)
