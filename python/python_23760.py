# 'User' object is not iterable
user = User.objects.get(username__iexact='username')
return render_to_response('timeline.html', {'tweets': user.tweets})
