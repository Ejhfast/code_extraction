# Not able to redirect to view after login
action="/login/{% if request.GET.next %}?next={{ request.GET.next }}{% endif %}"
