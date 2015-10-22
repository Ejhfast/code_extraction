# Django: Getting data associated with logged in user.
drafts = Draft.objects.filter(user=request.user)
