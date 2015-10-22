# Trouble validating a form in django
qs = OptionVote.objects.all()
form = OptionVoteForm(qs, request.POST)
