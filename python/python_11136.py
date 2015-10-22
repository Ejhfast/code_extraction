# Pythonic way to simplify this long Django view?
error_messages = {'post_title':'post title','post_text':'post text','publish':'publication status'}
errors = [error_messages[key] for key in ('post_title','post_text','publish') if not request.POST.has_key(key)]
