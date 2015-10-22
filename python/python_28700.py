# Django: 'AnonymousUser' object has no attribute 'get_full_name'
request.user.get_full_name() if request.user.is_authenticated() else ""
