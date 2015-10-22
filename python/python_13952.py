# TypeError: object of type 'instancemethod' has no len()
envelopes = Envelope.objects.filter(user=request.user).exclude_unallocated()
